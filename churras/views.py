from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    pratos = { 
        1:'Picanha', 
        2: 'Maminha',
        3: 'Fraldinha',
    }


    contexto = {
        'lista_pratos': pratos,

    }

    return render(request, 'index.html', contexto)
    #return HttpResponse('<h1>Churrasco Canes-Grill</h1>')
