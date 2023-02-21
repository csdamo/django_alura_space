from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from galeria.models import Fotografia, Categoria

def index(request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    categorias = Categoria.objects.all()
    context = {
        'fotografias': fotografias, 
        'categorias': categorias
    }
    return render(request, 'galeria/index.html', context=context)

def imagem (request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar (request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    termo_pesquisa = None
    if request.GET.get('buscar'):
        termo_pesquisa = request.GET.get('buscar')
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True).filter(nome__icontains=termo_pesquisa)
    categorias = Categoria.objects.all()
    context = {
        'fotografias': fotografias, 
        'categorias': categorias
    }
    return render(request, 'galeria/index.html', context=context)

def filtro_tags(request, categoria_id):
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True).filter(categoria=categoria_id)
    categorias = Categoria.objects.all()
    context = {
        'fotografias': fotografias, 
        'categorias': categorias
    }
    return render(request, 'galeria/index.html', context=context)
    