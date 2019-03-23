from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1> Expenditure </h1>")

def add(request):
    return HttpResponse("<h1> Adding Expenditure </h1>")