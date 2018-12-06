from .models import Prenda
from rest_framework import viewsets
from .serializers import PrendaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def prendaView(request, format=None):
    """
    List all code prendas, or create a new prenda.
    """
    if request.method == 'GET':
        prendas = Prenda.objects.all()
        serializer = PrendaSerializer
        return Response(serializer(context={'request': request}).data)

    elif request.method == 'POST':
        serializer = PrendaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def prenda_detail(request, pk):
    """
    Retrieve, update or delete a code prenda.
    """
    try:
        prenda = prenda.objects.get(pk=pk)
    except prenda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PrendaSerializer(prenda)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PrendaSerializer(prenda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prenda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
