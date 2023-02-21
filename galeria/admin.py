from django.contrib import admin
from .models import Categoria, Fotografia


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10 
    
    
admin.site.register(Categoria, CategoriaAdmin)


class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'categoria', 'usuario', 'publicada')
    list_display_links = ('id', 'nome', 'categoria', 'legenda', 'usuario',)
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10
    
    
admin.site.register(Fotografia, FotografiaAdmin)