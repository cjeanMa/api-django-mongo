from rest_framework import serializers
from .models import Publicaciones

class PublicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Publicaciones
        fields=('id',
                'author',
                'nationality',
                'title',
                'description',
                'pages',
                'published')