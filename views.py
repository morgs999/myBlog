# mysite/views.py

from django.http import HttpResponse

def index(request):
    """simple intro message"""
    return HttpResponse("Welcome to the Morgan Clarke blog.")
