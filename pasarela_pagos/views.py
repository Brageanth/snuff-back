from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json

@api_view(['GET', 'POST'])
def consulta_bancos(request):
    if request.method == 'GET':
        data = {
   "test": false,
   "language": "es",
   "command": "GET_PAYMENT_METHODS",
   "merchant": {
      "apiLogin": "pRRXKOl8ikMmt9u",
      "apiKey": "4Vj8eK4rloUd272L48hsrarnUA"
   }
}
        encoded_data = json.dumps(data).encode('utf-8')
        return Response(requests.post('https://sandbox.api.payulatam.com/reports-api/4.0/service.cgi', data=encoded_data, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}))