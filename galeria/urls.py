from django.urls import path
from .views import buscar, filtro_tags, index, imagem, favorito, mais_votados, meus_favoritos

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('filtro_tags/<int:categoria_id>', filtro_tags, name='filtro_tags'),
    path('favorito/<int:foto_id>', favorito, name='favorito'),
    path('mais_votados', mais_votados, name='mais_votados'),
    path('meus_favoritos', meus_favoritos, name='meus_favoritos'),
]
