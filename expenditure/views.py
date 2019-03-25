from django.shortcuts import render
from django.http import HttpResponse

expenditures = [
    {
        'name': 'Netflix',
        'price': 10.99
    },
    {
        'name': 'Amazon',
        'price': 7.99
    },
    {
        'name': 'Xtra-Fit',
        'price': 15.00
    }

]


def home(request):

    monthly_payment = 0.0

    for i, price in enumerate(d['price'] for d in expenditures):
        monthly_payment += price

    monthly_payment = '%.3f'%(monthly_payment)
    context = {
        'expenditures': expenditures,
        'monthly_payment': monthly_payment
    }
    return render(request, 'expenditure/home.html', context)


