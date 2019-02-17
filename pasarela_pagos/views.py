from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
import requests
import json

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
        return requests.post('https://api.payulatam.com/reports-api/4.0/service.cgi', data=encoded_data)