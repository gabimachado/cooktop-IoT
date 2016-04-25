#Authors: Gabriella Machado and Natalie Bezerra

from myapp.models import Mode, State
from rest_framework import viewsets
from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.serializers import ModeSerializer, StateSerializer
import requests
import json

class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

def home(request):
    out = ''
    currentmode = 'manual'
    currentstate = 'off'

    if 'low' in request.POST:
        values = {"name": "low"}
        r = requests.put('http://127.0.0.1:8000/state/1/',
                        data=values, auth=('username', 'password'))
        result = r.text
        output = json.loads(result)
        out = output['name']
        
    if 'medium' in request.POST:
        values = {"name": "medium"}
        r = requests.put('http://127.0.0.1:8000/state/1/',
                        data=values, auth=('username', 'password'))
        result = r.text
        output = json.loads(result)
        out = output['name']

    if 'high' in request.POST:
        values = {"name": "high"}
        r = requests.put('http://127.0.0.1:8000/state/1/',
                        data=values, auth=('username', 'password'))
        result = r.text
        output = json.loads(result)
        out = output['name']
        
    if 'off' in request.POST:
        values = {"name": "off"}
        r = requests.put('http://127.0.0.1:8000/state/1/',
                        data=values, auth=('username', 'password'))
        result = r.text
        output = json.loads(result)
        out = output['name']
        
    if 'auto' in request.POST:
        values = {"name": "auto"}
        r = requests.put('http://127.0.0.1:8000/mode/1/',
                        data=values, auth=('username', 'password'))
        result = r.text
        output = json.loads(result)
        out = output['name']
        
    if 'manual' in request.POST:
        values = {"name": "manual"}
        r = requests.put('http://127.0.0.1:8000/mode/1/',
                        data=values, auth=('username', 'password'))
        result = r.text
        output = json.loads(result)
        out = output['name']

    r = requests.get('http://127.0.0.1:8000/mode/1/',
                    auth=('username', 'password'))
    result = r.text
    output = json.loads(result)
    currentmode = output['name']

    r = requests.get('http://127.0.0.1:8000/state/1/',
                    auth=('username', 'password'))
    result = r.text
    output = json.loads(result)
    currentstate = output['name']

    return render_to_response('myapp/index.html', {'name':out,
    'currentmode':currentmode, 'currentstate':currentstate},
    context_instance=RequestContext(request))
