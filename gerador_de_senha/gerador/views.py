from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random
import string

def gerador(request):
    template = loader.get_template('index.html')

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(16))

    response = {"senha" : senha,}


    return HttpResponse(template.render(response, request))

# Create your views here.
