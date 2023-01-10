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
        id_list = [data[i]['record_id'] for i in range(len(data))]
        return Record.objects.filter(id__in=id_list)


record_detail_view = RecordDetailAPIView.as_view()


class RecordForQueryListAPIView(generics.ListAPIView):
    serializer_class = RecordForQuerySerializer

    def get_queryset(self):
        """
        This view should return a list of all the records ids associated with a particular query id.
        """
        id_req = self.request.query_params.get('id')
        return RecordForQuery.objects.filter(query_id=id_req)


record_list_view = RecordForQueryListAPIView.as_view()
