from .models import Empresa
from rest_framework import viewsets
from .serializers import EmpresaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def empresaView(request, format=None):
    """
    List all code empresa, or create a new empresa.
    """
    if request.method == 'GET':
        empresa = Empresa.objects.all()
        serializer = EmpresaSerializer
        return Response(serializer(empresa, many=True).data)

    elif request.method == 'POST':
        serializer = EmpresaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def empresa_detail(request, pk):
    """
    Retrieve, update or delete a code empresa.
    """
    try:
        empresa = empresa.objects.get(pk=pk)
    except empresa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)