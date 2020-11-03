from django.http import HttpResponse

def hello_world(request):
    """ Greeting """
    return HttpResponse("Hello World!")
