from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1 style='background-color: aqua; text-align: center;' >Success!</h1>")