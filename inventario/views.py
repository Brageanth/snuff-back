from .models import Prenda, Colore, Talla, Estampado
from rest_framework import viewsets
from .serializers import PrendaSerializer, ColorSerializer, TallaSerializer, EstampadoSerializer
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
        return Response(serializer(prendas, many=True).data)

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


@api_view(['GET', 'POST'])
def colorView(request, format=None):
    if request.method == 'GET':
        color = Colore.objects.all()
        serializer = ColorSerializer
        return Response(serializer(color, many=True).data)

    elif request.method == 'POST':
        serializer = ColorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def color_detail(request, pk):
    try:
        color = Color.objects.get(pk=pk)
    except color.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ColorSerializer(color)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ColorSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def tallaView(request, format=None):
    if request.method == 'GET':
        talla = Talla.objects.all()
        serializer = TallaSerializer
        return Response(serializer(talla, many=True).data)

    elif request.method == 'POST':
        serializer = TallaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def talla_detail(request, pk):
    try:
        talla = Talla.objects.get(pk=pk)
    except talla.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TallaSerializer(talla)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TallaSerializer(talla, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        talla.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def estampadoView(request, format=None):
    if request.method == 'GET':
        estampado = Estampado.objects.all()
        serializer = EstampadoSerializer
        return Response(serializer(estampado, many=True).data)

    elif request.method == 'POST':
        serializer = EstampadoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def estampado_detail(request, pk):
    try:
        estampado = Estampado.objects.get(pk=pk)
    except estampado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EstampadoSerializer(estampado)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EstampadoSerializer(estampado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        estampado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
