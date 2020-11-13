from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Publicaciones
from .serializers import PublicacionesSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def publicaciones_list(request):
    if request.method == 'GET':
        publicaciones = Publicaciones.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            publicaciones = publicaciones.filter(title__icontains=title)
        publicaciones_serializer = PublicacionesSerializer(publicaciones, many=True)
        return JsonResponse(publicaciones_serializer.data, safe=False)
    elif request.method=='POST':
        publicacion_data = JSONParser().parse(request)
        publicaciones_serializer = PublicacionesSerializer(data=publicacion_data)
        if publicaciones_serializer.is_valid():
            publicaciones_serializer.save()
            return JsonResponse(publicaciones_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(publicaciones_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        count = Publicaciones.objects.all().delete()
        return JsonResponse({'message': '{} Cantidad de Tutoriales Borrados'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def publicacion_detail(request,pk):
    try:
        publicacion = Publicaciones.objects.get(pk=pk)
    except Publicaciones.DoesNotExist:
        return  JsonResponse({'message': "Dicha Publicacion no existe"}, status=status.HTTP_404_BAD_REQUEST)

    if request.method == 'GET':
        publicacion_serializer = PublicacionesSerializer(publicacion)
        return JsonResponse(publicacion_serializer.data)

    elif request.method == 'PUT':
        publicacion_data = JSONParser().parse(request)
        publicacion_serializer = PublicacionesSerializer(publicacion, data=publicacion_data)
        if publicacion_serializer.is_valid():
            publicacion_serializer.save()
            return JsonResponse(publicacion_serializer.data)
        return JsonResponse(publicacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        publicacion.delete()
        return JsonResponse({"message": "Tutorial Eliminado"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def publicaciones_list_published(request):
    publicacion = Publicaciones.objects.filter(published=True)
    if request.method == 'GET':
        publicacion_serializer = PublicacionesSerializer(publicacion, many=True)
        return JsonResponse(publicacion_serializer.data, safe=False)
