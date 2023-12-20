from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    return HttpResponse("hrllo")
def login(request):
    return render(request, 'login.html')