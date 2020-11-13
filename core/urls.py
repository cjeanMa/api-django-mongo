from django.urls import path
from .views import *

urlpatterns = [
    path('api/publicaciones/', publicaciones_list),
    path('api/publicaciones/<pk>', publicacion_detail),
    path('api/publisheds/', publicaciones_list_published),
]
