from django.http import HttpResponse
from django.shortcuts import render
from .db_articles import articles # du dossier courant prend db_articles et importes les articles
#from . import db_articles

def home_view(request): # ce parametre request est obligatoire
    #return HttpResponse('hello world')
    return render(request, 'home.html')

def contact_view(request):
    #return HttpResponse('contacter nous')
    return render(request, 'contact.html')

def articles_view(request):
    return render(request, 'articles.html', context={
        'articles': articles
    })