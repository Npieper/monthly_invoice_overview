from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'expenditure/home.html')

def add(request):
    return HttpResponse("<h1> Adding Expenditure </h1>")