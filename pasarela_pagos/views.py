from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def consulta_bancos(requests):
    if request.method == 'GET':
        r = requests.post("https://sandbox.api.payulatam.com/payments-api/4.0/service.cgi", data={
            "test": true,
            "language": "es",
            "command": "PING",
            "merchant": {
                "apiLogin": "pRRXKOl8ikMmt9u",
                "apiKey": "4Vj8eK4rloUd272L48hsrarnUA"
            }
        })
        return Response(r)