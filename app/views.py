# Django
from django.http import HttpResponse

# Utilities (Doesn't part of Django)
from datetime import datetime

def hello_world(request):
    """ Greeting """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f"Server Current Time is {now}")
