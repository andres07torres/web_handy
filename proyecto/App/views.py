from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'reconocimiento.html')

def funcionamiento(request):
    return render(request, 'funcionamiento.html')

def buscar(request):
    # .lower() convierte todo a minúsculas para que "Inicio" y "inicio" sean lo mismo
    query = request.GET.get('q', '').lower().strip()
    
    if not query:
        return redirect('index')

    rutas_map = {
        'index': ['inicio', 'home', 'casa', 'principal'],
        'funcionamiento': ['funciona', 'como', 'tutorial', 'instrucciones']
    }

    for ruta, palabras in rutas_map.items():
        for palabra in palabras:
            if palabra in query:
                return redirect(ruta)

    # Si no encuentra nada, vuelve al inicio
    return redirect('index')