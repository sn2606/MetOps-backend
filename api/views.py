from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from query.models import MetQuery
from query.serializers import MetQuerySerializer

# Create your views here.


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = MetQuerySerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
