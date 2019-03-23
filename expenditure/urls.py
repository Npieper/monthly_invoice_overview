from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="expenditure-home"),
    path('add/', views.add, name="expenditure-add")

]
