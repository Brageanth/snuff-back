from .models import Personalizada
from rest_framework import viewsets
from .serializers import PersonalizadaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def personalizadaView(request, format=None):
    """
    List all code personalizadas, or create a new personalizada.
    """
    if request.method == 'GET':
        personalizadas = Personalizada.objects.all()
        serializer = PersonalizadaSerializer
        return Response(serializer(personalizadas, many=True).data)

    elif request.method == 'POST':
        serializer = PersonalizadaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def personalizada_detail(request, pk):
    """
    Retrieve, update or delete a code personalizada.
    """
    try:
        personalizada = Personalizada.objects.get(pk=pk)
    except personalizada.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonalizadaSerializer(personalizada)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonalizadaSerializer(personalizada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        personalizada.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
