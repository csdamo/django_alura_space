from django.urls import path
from .views import buscar, filtro_tags, index, imagem, favorito

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('filtro_tags/<int:categoria_id>', filtro_tags, name='filtro_tags'),
    path('favorito/<int:foto_id>', favorito, name='favorito'),
]
