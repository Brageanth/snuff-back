from .models import Campania
from rest_framework import viewsets
from .serializers import CampaniaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def campaniaView(request, format=None):
    """
    List all code campania, or create a new campania.
    """
    if request.method == 'GET':
        campania = Campania.objects.all()
        serializer = CampaniaSerializer
        return Response(serializer(campania, many=True).data)

    elif request.method == 'POST':
        serializer = CampaniaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def campania_detail(request, pk):
    """
    Retrieve, update or delete a code campania.
    """
    try:
        campania = campania.objects.get(pk=pk)
    except campania.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CampaniaSerializer(campania)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CampaniaSerializer(campania, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        campania.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)