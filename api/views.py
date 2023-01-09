from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.records.models import Record

# Create your views here.


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    model_data = Record.objects.all().order_by("?").first()
    return Response(model_data)
