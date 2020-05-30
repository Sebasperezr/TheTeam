"""TheTeam Vistas."""
#django
from django.http import HttpResponse

#utilidades
from datetime import datetime
import json

def holi1(request):
    print(request)
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, La fecha es  {now}'.format(now=str(now)))

def holi(request):
    numbers = [int(i) for i in request.GET['numeros'].split(',')]
    sorted_ints = sorted(numbers)
    data= {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
    