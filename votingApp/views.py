from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(response):
    return HttpResponse("Welcome to the voting app")

def time(request):
    return HttpResponse(datetime.datetime .now().date())



# Create your views here.
