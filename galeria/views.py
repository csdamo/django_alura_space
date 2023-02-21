from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from galeria.models import Fotografia, Categoria

def index(request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    categorias = Categoria.objects.all()
    user_id = request.user

    context = {
        'fotografias': fotografias, 
        'categorias': categorias,
        'user_id': user_id
    }
    return render(request, 'galeria/index.html', context=context)

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar (request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    termo_pesquisa = ''
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

def favorito(request, foto_id):
    user_id = request.user.id
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    favorito = fotografia.favorito.filter(user=user_id)
    total_favoritos = fotografia.total_favoritos
    
    if favorito:
       fotografia.favorito.remove(user_id)
       fotografia.total_favoritos = int(total_favoritos) - 1
    else:
        fotografia.favorito.add(user_id)
        fotografia.total_favoritos = int(total_favoritos) + 1
    fotografia.save()
    return redirect ('index')

def mais_votados(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-total_favoritos').filter(publicada=True)[:3]
    categorias = Categoria.objects.all()
    user_id = request.user

    context = {
        'fotografias': fotografias, 
        'categorias': categorias,
        'user_id': user_id
    }
    return render(request, 'galeria/index.html', context=context)

def meus_favoritos(request):
    user_id = request.user.id
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
   
    fotografias = Fotografia.objects.order_by('-total_favoritos').filter(favorito=user_id)
    categorias = Categoria.objects.all()
    user_id = request.user

    context = {
        'fotografias': fotografias, 
        'categorias': categorias,
        'user_id': user_id
    }
    return render(request, 'galeria/index.html', context=context)
