from random import uniform
from re import split, findall
import requests
import os
from dotenv import read_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
read_dotenv(dotenv_path)


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
    pmls.extend(
        [f'relative_humidity_{invl*(i+1)}m:p' for i in range(steps)])
    pmls.extend([f'pressure_{invl*(i+1)}m:hPa' for i in range(steps)])
    pmls.extend([f'wind_speed_{invl*(i+1)}m:kmh' for i in range(steps)])
    pmls.extend([f'wind_dir_{invl*(i+1)}m:d' for i in range(steps)])
    return pmls


def generate_random_data_response(latitude: float, longitude: float, parameters: list, date: str, username: str):
    """
    Dummy Function that returns a dict in the same format as meteomatics api
    Used since Meteomatics API free version does not provide enough upper air data
    """
    data = []
    # no of parameters from each entity
    # 5 entities - T, P, rH, wind_speed, wind_dir
    n = int(len(parameters)/5)
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


def virtual_temp(temperature, pressure, relative_humidity):
    """
    Return Virtual Temperature given Temperature, Pressure and Relative Humidity
    """
    T = float(temperature)
    p = float(pressure)
    rh = float(relative_humidity)
    exp = 7.5*(T/(T + 237.7))
    es = 6.11 * pow(10, exp)
    ws = 621.9569100577033 * (es/(p - es))
    w = rh * ws
    vt = T * ((w + 0.6219569100577033)/(0.6219569100577033 * (1 + w)))
    return vt


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

    virtual_temperature = [virtual_temp(
        temperature[i], pressure[i], relative_humidity[i]) for i in range(n)]

    records = [{
        'height': height[i],
        'temperature': temperature[i],
        'virtual_temperature': virtual_temperature[i],
        'pressure': pressure[i],
        'relative_humidity': relative_humidity[i],
        'wind_speed': wind_speed[i],
        'wind_direction': wind_direction[i]
    } for i in range(n)]

    result = {
        'status': 200,
        'latitude': latitude,
        'longitude': longitude,
        'records': records
    }

    return result


def location(latitude, longitude):
    """
    Get location from latitude and longitude.
    """
    access_key = str(os.getenv('POSITIONSTACK_API_KEY'))
    url = f'http://api.positionstack.com/v1/reverse?access_key={access_key}&query={latitude},{longitude}&limit=2&output=json'
    res = requests.get(url).json()
    if res['data']:
        location = f"{res['data'][0]['county']}, {res['data'][0]['region']}"
        return location
    else:
        return ''
