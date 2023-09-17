from django.shortcuts import get_object_or_404
from rest_framework import views, status
from rest_framework.response import Response
from . import api_requests

class CurrencyConverterView(views.APIView):
    '''api представление запроса на конвертацию'''
    def get(self, request):
        from_currency = self.request.query_params.get('from')
        to_currency = self.request.query_params.get('to')
        value = int(self.request.query_params.get('value', 1))
        result = api_requests.get_currency(from_currency,to_currency,value)
        if result['success']:
            return Response({"result": result['result']}, status=status.HTTP_200_OK)
        else:
            return Response({"error": result['error']}, status=status.HTTP_404_NOT_FOUND)
        
class ListOfRates(views.APIView):
    '''Список всех курсов к базовой валюте'''
    def get(self,request):
        currency = self.request.query_params.get('base')
        result = api_requests.list_of_rates(currency=currency)
        if result['success']:
            return Response({"result": result['list']}, status=status.HTTP_200_OK)
        else:
            return Response({"error": result['error']}, status=status.HTTP_404_NOT_FOUND)