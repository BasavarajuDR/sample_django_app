from django.shortcuts import render
import traceback
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from models import *

@csrf_exempt
def get_factorial(request):
    res = {'success' : False, 'message' : ''}

    if request.method != 'POST':
        return HttpResponseBadRequest()

    try:
        params = json.loads(request.body)

        if 'number' in params:
            res = Factorial.run(params['number'])
        else:
            res['message'] = 'Number is empty'

    except Exception as e:
        res['message'] = str(e)
        traceback.print_exc()

    return HttpResponse(json.dumps(res),'application/json')