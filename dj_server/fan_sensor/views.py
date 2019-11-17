from django.shortcuts import render

# Create your views here.
import json
import ast
import requests

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Sensor, WorkerCoordinate

man_under_fan = False


@csrf_exempt
@require_http_methods(['PUT', 'POST'])
def index(request):
    if request.method == 'POST':
        data = request.body
        decoded_data = json.loads(data)
        decoded_data = dict(ast.literal_eval(decoded_data))

        need_enable_fan = decoded_data['smoke']
        global man_under_fan
        if need_enable_fan and man_under_fan:
            url = 'http://127.0.0.1:5500'
            data = {"command": "enable"}
            serialized_data = json.dumps(data)

            requests.post(url, json=serialized_data)

    if request.method == 'PUT':
        in_room = request.body
        if in_room:
            global man_under_fan
            man_under_fan = True
        else:
            global man_under_fan
            man_under_fan = False
        return HttpResponse('z')
