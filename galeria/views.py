from django.shortcuts import get_object_or_404, render

from galeria.models import Fotografia

def index(request):
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    
    return render(request, 'galeria/index.html', {'fotografias': fotografias})

def imagem (request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})


def buscar (request):
    termo_pesquisa = None
    if request.GET.get('buscar'):
        termo_pesquisa = request.GET.get('buscar')
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True).filter(nome__icontains=termo_pesquisa)
    
    return render(request, 'galeria/index.html', {'fotografias': fotografias})