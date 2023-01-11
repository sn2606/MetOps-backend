from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import uniform
from re import split, findall
from datetime import datetime
# import meteomatics.api

from .models import MetQuery, QueryForUser
from .serializers import MetQuerySerializer, QueryForUserSerializer
from records.models import Record, RecordForQuery
from records.serializers import RecordSerializer, RecordForQuerySerializer


def generate_random_data_response(latitude: float, longitude: float, parameters: list, date: str, username: str):
    """
    Dummy Function that returns a dict in the same format as meteomatics api
    Used since Meteomatics API free version does not provide enough upper air data
    """
    data = []
    # no of parameters from each entity
    n = int(len(parameters)/5)  # 5 entities - T, P, rH, wind_speed, wind_dir
    range_entity_from_param = range(n)
    limits = {
        'C': sorted([uniform(-10.0, 50.0) for i in range_entity_from_param], reverse=True),
        'p': sorted([uniform(2.0, 100.0) for i in range_entity_from_param], reverse=True),
        'hPa': sorted([uniform(10.0, 20.0) for i in range_entity_from_param], reverse=True),
        'kmh': sorted([uniform(3.0, 12.0) for i in range_entity_from_param]),
        'd': sorted([uniform(0.0, 359.999) for i in range_entity_from_param])
    }

    for i in range(len(parameters)):
        unit = split('[:]', parameters[i])[1]
        data.append({
            'parameter': parameters[i],
            'coordinates': [
                {
                    'lat': latitude,
                    'lon': longitude,
                    'dates': [
                        {
                            'date': date,
                            'value': limits[unit][i % n]
                        }
                    ]
                }
            ]
        })

    # response value as given by meteomatics api
    response = {
        'version': '3.0',
        'user': username,
        'dateGenerated': date,
        'status': 'OK',
        'data': data
    }

    return response


def process_response_data(data, latitude: float, longitude: float, invl: int, max: int):
    """
    Function that takes meteomatics response JSON as input and gives output analogical to the record model
    """
    n = int(max/invl)

    height = [invl*(i+1) for i in range(n)]
    temperature = [0.0] * n
    pressure = [0.0] * n
    relative_humidity = [0.0] * n
    wind_speed = [50.0] * n
    wind_direction = [50.0] * n

    ud = {
        'C': temperature,
        'hPa': pressure,
        'p': relative_humidity,
        'kmh': wind_speed,
        'd': wind_direction
    }

    for reading in data['data']:
        param = reading['parameter']
        ht = list(map(int, findall(r'\d+', param)))[0]
        unit = split('[:]', param)[1]
        ud[unit][int(ht/invl)-1] = reading['coordinates'][0]['dates'][0]['value']

    records = [{
        'height': height[i],
        'temperature': temperature[i],
        'pressure': pressure[i],
        'relative_humidity': relative_humidity[i],
        'wind_speed': wind_speed[i],
        'wind_direction': wind_direction[i]
    } for i in range(n)]

    result = {
        'latitude': latitude,
        'longitude': longitude,
        'records': records
    }

    return result


def generate_parameter_list(invl, max):
    """
    Generate the list of parameters in format required for creating API get query URL
    Entities: Temperature, Relative Humidity, Pressure, Wind Speed, Wind Direction
    Takes input
        1. invl = interval value in meters, for altitude
        2. max = max altitude required
    Returns a list of parameter names
    """
    steps = int(max/invl)
    pmls = []
    pmls.extend([f't_{invl*(i+1)}m:C' for i in range(steps)])
    pmls.extend([f'relative_humidity_{invl*(i+1)}m:p' for i in range(steps)])
    pmls.extend([f'pressure_{invl*(i+1)}m:hPa' for i in range(steps)])
    pmls.extend([f'wind_speed_{invl*(i+1)}m:kmh' for i in range(steps)])
    pmls.extend([f'wind_dir_{invl*(i+1)}m:d' for i in range(steps)])
    return pmls


@api_view(["GET"])
def get_meteomatics_response(request, *args, **kwargs):
    latitude = request.query_params.get('latitude')
    longitude = request.query_params.get('longitude')
    username = 'armamentresearchanddevelopmentestablishment_nayak'
    datetimenow = datetime.utcnow().strftime('%Y-%d-%mT%H:%M:%SZ')
    parameters = generate_parameter_list(200, 20000)
    # url = f'https://api.meteomatics.com/{datetimenow}--{datetimenow}/{",".join(parameters)}/{latitude},{longitude}/json?model=mix'
    # response = meteomatics.api.query_api(
    #     url=url, username=username, password=password, request_type="GET")
    try:
        response = generate_random_data_response(
            latitude=latitude, longitude=longitude, parameters=parameters, date=datetimenow, username=username)
        result = process_response_data(
            data=response, latitude=latitude, longitude=longitude, invl=200, max=20000)
        return Response(result)
    except:
        return Response('Sorry, some error occured on our side')

# class QueryListAPIView(generics.ListAPIView):
