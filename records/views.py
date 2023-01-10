from rest_framework import generics

from query.models import MetQuery, QueryForUser
from query.serializers import MetQuerySerializer, QueryForUserSerializer
from .models import Record, RecordForQuery
from .serializers import RecordSerializer, RecordForQuerySerializer


class RecordDetailAPIView(generics.ListAPIView):
    serializer_class = RecordSerializer

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

    def get_queryset(self):
        """
        This view should return a list of all the records ids associated with a particular query id.
        """
        query_id_req = self.request.query_params.get('queryid')
        return RecordForQuery.objects.filter(query_id=query_id_req)


record_list_view = RecordForQueryListAPIView.as_view()


class RecordCreateAPIView(generics.CreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def perform_create(self, serializer):
        record_instance = serializer.save()
        queryid = self.request.query_params.get('query_id')
        query_instance = MetQuery.objects.get(id=queryid)
        if record_instance:
            RecordForQuery.objects.create(
                query_id=query_instance, record_id=record_instance)


record_create_view = RecordCreateAPIView.as_view()
