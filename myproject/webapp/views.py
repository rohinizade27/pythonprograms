from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return HttpResponse("<h2>welcome to bridgelabz solution..<h2/>")
