from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add,mul, xsum

def index(request, id=None):
    a = add.delay(5,3)
    print(a)
    return HttpResponse("Hello World!")


