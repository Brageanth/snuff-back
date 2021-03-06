from .models import Usuario
from rest_framework import viewsets
from .serializers import UsuarioSerializer, ResetSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import EmailMessage
from random import randint


@api_view(['GET', 'POST'])
def resetPassword(request, format=None):
    """
    List all code usuarios, or create a new usuario.
    """
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = ResetSerializer
        return Response(serializer(context={'request': request}).data)

    elif request.method == 'POST':
        serializer = ResetSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            mailAddress=serializer.data["correo"]
            if Usuario.objects.filter(correo=mailAddress).exists():
                codigo = randint(1000, 9999)
                asunto = "Codigo para restablecer tu contraseña de Snuff"
                mensaje = str(codigo)
                mail = EmailMessage(asunto, mensaje, to=[mailAddress])
                mail.send()
                return Response(codigo, status=status.HTTP_201_CREATED)
            else:
                return Response(codigo, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def usuarioView(request, format=None):
    """
    List all code usuarios, or create a new usuario.
    """
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer
        return Response(serializer(usuarios, many=True).data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, pk):
    """
    Retrieve, update or delete a code usuario.
    """
    try:
        usuario = Usuario.objects.get(pk=pk)
    except usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        return Response(status=status.HTTP_400_BAD_REQUEST)
