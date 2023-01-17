from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
# import meteomatics.api

from .utils import *
from .models import MetQuery, QueryForUser
from .serializers import MetQuerySerializer, QueryForUserSerializer
from records.models import Record, RecordForQuery
from records.serializers import RecordSerializer, RecordForQuerySerializer


class QueryResponse(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            latitude = request.query_params.get('latitude')
            longitude = request.query_params.get('longitude')
            invl = 100
            max = 20000
            if latitude and longitude:
                pass
            else:
                raise Exception('Please provide latitude and longitude')
            username = 'armamentresearchanddevelopmentestablishment_nayak'
            datetimenow = datetime.utcnow().strftime('%Y-%d-%mT%H:%M:%SZ')
            parameters = generate_parameter_list(invl, max)
            try:
                # url = f'https://api.meteomatics.com/{datetimenow}--{datetimenow}/{",".join(parameters)}/{latitude},{longitude}/json?model=mix'
                # response = meteomatics.api.query_api(
                #     url=url, username=username, password=password, request_type="GET")
                response = generate_random_data_response(
                    latitude=latitude, longitude=longitude, parameters=parameters, date=datetimenow, username=username)
                result = process_response_data(
                    data=response, latitude=latitude, longitude=longitude, invl=invl, max=max)
                return Response(result)
            except:
                return Response('Sorry, some error occured on our side')
        except Exception as e:
            return Response(str(e), status=404)


query_response_view = QueryResponse.as_view()


class QueryListAPIView(generics.ListAPIView):
    serializer_class = MetQuerySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get('userid')
        query_id_list = list(
            map(lambda elem: elem.id, QueryForUser.objects.filter(user_id=user_id)))
        return MetQuery.objects.filter(id__in=query_id_list).order_by('-created')


query_list_view = QueryListAPIView.as_view()


class QueryResponseSaveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # print(request)
        try:
            user_id = request.data['user']['userid']
            latitude = request.data['query']['latitude']
            longitude = request.data['query']['longitude']
            query_data = {
                'latitude': latitude,
                'longitude': longitude,
                'location': location(latitude, longitude)
            }
            record_list = request.data['records']
            # print(record_list)
            serialized = MetQuerySerializer(data=query_data)
            if serialized.is_valid(raise_exception=True):
                saved_query = serialized.save()
                query_id = saved_query.id
                serialized = QueryForUserSerializer(
                    data={'user_id': user_id, 'query_id': query_id})
                if serialized.is_valid(raise_exception=True):
                    serialized.save()
                    serialized = RecordSerializer(data=record_list, many=True)
                    if serialized.is_valid(raise_exception=True):
                        saved_records = serialized.save()
                        record_for_query_list = list(map(
                            lambda rec: {'query_id': query_id, 'record_id': rec.id}, saved_records))
                        serialized = RecordForQuerySerializer(
                            data=record_for_query_list, many=True)
                        if serialized.is_valid(raise_exception=True):
                            serialized.save()
                            return Response({'status': 200})
        except Exception as e:
            print(e)
            return Response({'status': 400})


query_save_view = QueryResponseSaveView.as_view()
