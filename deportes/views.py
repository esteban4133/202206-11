from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader

# Create your views here.


def index (request):
    
    template = loader.get_template('deportes/index.html')
  
   # return HttpResponse(template.render(request))
    return render(request,'deportes/index.html')
