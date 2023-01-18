from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from query.models import MetQuery, QueryForUser
from query.serializers import MetQuerySerializer, QueryForUserSerializer
from .models import Record, RecordForQuery
from .serializers import RecordSerializer, RecordForQuerySerializer


class RecordDetailAPIView(generics.ListAPIView):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the records associated filtered by the record id.
        """
        request = self.request
        data = record_list_view(request=request._request).data
        record_id_list = [data[i]['record_id'] for i in range(len(data))]
        return Record.objects.filter(id__in=record_id_list)


record_detail_view = RecordDetailAPIView.as_view()


class RecordForQueryListAPIView(generics.ListAPIView):
    serializer_class = RecordForQuerySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the records ids associated with a particular query id.
        """
        query_id_req = self.request.query_params.get('queryid')
        return RecordForQuery.objects.filter(query_id=query_id_req)


record_list_view = RecordForQueryListAPIView.as_view()


class RecordDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None):
        query_id = request.data['queryid']
        query = MetQuery.objects.get(id=query_id)
        query.delete()
        record_id_list = request.data['recordid']
        records = Record.objects.filter(id__in=record_id_list)
        map(lambda item: item.delete(), records)
        return Response('Done')


record_delete_view = RecordDeleteView.as_view()
