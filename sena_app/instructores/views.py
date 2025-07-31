from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Instructor

def instructores(request):
    lista_instructores = Instructor.objects.all()
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))