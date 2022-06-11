from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader

from familia.forms import Persona1
from familia.models import individuo




def index (request):
    personas = individuo.objects.all()
    template = loader.get_template('familia/index.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))

def listado (request):
    personas = individuo.objects.all()
    template = loader.get_template('familia/listado_familia.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))


def inicio (request):
    personas = individuo.objects.all()
    template = loader.get_template('familia/index.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))



def agregar (request):
    if request.method == "POST":
        form = Persona1(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            altura = form.cleaned_data['altura']
            individuo(nombre=nombre,fecha_nacimiento=fecha_nacimiento,altura=altura).save()

            return HttpResponseRedirect("/familia/")

    elif request.method == "GET":
        form = new_func()
       
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


    return render(request, 'familia/cargar.html', {'form': form})

def new_func():
    form = Persona1()
    return form

def deportes (request):

     return render(request,'deportes/index.html')
    