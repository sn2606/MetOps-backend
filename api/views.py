from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from query.models import MetQuery
from query.serializers import MetQuerySerializer
from records.models import Record
from records.serializers import RecordSerializer

# Create your views here.


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    instance = Record.objects.first()
    if instance:
        data = RecordSerializer(instance).data
        return Response(data)
