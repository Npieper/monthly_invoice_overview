from django.shortcuts import render
from django.http import HttpResponse
from .models import Expenditure


def home(request):

    expenditures = Expenditure.objects.all()
    monthly_payment = calculate_monthly_payment(expenditures)

    context = {
        'expenditures': expenditures,
        'monthly_payment': monthly_payment
    }

    return render(request, 'expenditure/expenditure.html', context)

def calculate_monthly_payment(expenditures):

    monthly_payment = 0.0

    for expenditure in expenditures:
        monthly_payment += expenditure.price

    monthly_payment = '%.3f'%(monthly_payment)

    return monthly_payment