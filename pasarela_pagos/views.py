from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib3
import json

http = urllib3.PoolManager()

@api_view(['GET', 'POST'])
def consulta_bancos(request):
    if request.method == 'GET':
        data = {
            "test": True,
            "language": "es",
            "command": "PING",
            "merchant": {
                "apiLogin": "pRRXKOl8ikMmt9u",
                "apiKey": "4Vj8eK4rloUd272L48hsrarnUA"
            }
        }
        encoded_data = json.dumps(data).encode('utf-8')
        r = http.request('POST', 'https://sandbox.api.payulatam.com/reports-api/4.0/service.cgi', body=data, headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        print(r)
        return Response(r)