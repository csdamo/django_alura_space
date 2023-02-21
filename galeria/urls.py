from django.urls import path
from .views import buscar, filtro_tags, index, imagem, favorito, mais_votados, meus_favoritos, minhas_fotos, fotos_usuario, mais_visualizadas

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('filtro_tags/<int:categoria_id>', filtro_tags, name='filtro_tags'),
    path('favorito/<int:foto_id>', favorito, name='favorito'),
    path('mais_votados', mais_votados, name='mais_votados'),
    path('meus_favoritos', meus_favoritos, name='meus_favoritos'),
    path('minhas_fotos', minhas_fotos, name='minhas_fotos'),
    path('fotos_usuario/<int:user_id>', fotos_usuario, name='fotos_usuario'),
    path('mais_visualizadas', mais_visualizadas, name='mais_visualizadas'),
]
