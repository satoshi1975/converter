from django.urls import path
from .views import CurrencyConverterView, ListOfRates

urlpatterns = [
    path('converter/', CurrencyConverterView.as_view(),
         name='convertation'),  # запрос на конвертацию из одной валюты в другую
    path('rates/', ListOfRates.as_view(),
         name='rates'),  # запрос на список курсов к базовой валюте
]