from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods


json_data = {
    "signal": {
        "state": "True"
    }
}
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return JsonResponse(json_data)
    return HttpResponse("Hello, world. You're at the polls index.")
