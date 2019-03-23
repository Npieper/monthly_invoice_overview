from django.shortcuts import render
from django.http import HttpResponse

expenditures = [
    {
        'netflix': 10.99,
        'amazon': 7.99,
        'xtra_fit': 15
    }
]


def home(request):
    context = {
        'expenditures': expenditures
    }
    return render(request, 'expenditure/home.html', context)


def add(request):
    return HttpResponse("<h1> Adding Expenditure </h1>")
