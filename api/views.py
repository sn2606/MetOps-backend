import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = request.GET
    data['content_type'] = request.content_type
    data['headers'] = dict(request.headers)
    print(data)
    return JsonResponse(data)
