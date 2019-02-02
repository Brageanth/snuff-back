from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib3

http = urllib3.PoolManager()

@api_view(['GET', 'POST'])
def consulta_bancos(self):
    if request.method == 'GET':
        r = http.request('POST', 'https://sandbox.api.payulatam.com/payments-api/4.0/service.cgi', body={
            "test": true,
            "language": "es",
            "command": "PING",
            "merchant": {
                "apiLogin": "pRRXKOl8ikMmt9u",
                "apiKey": "4Vj8eK4rloUd272L48hsrarnUA"
            }
        }, headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        return Response(r)