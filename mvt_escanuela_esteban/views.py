from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader


def index (request):
    
    template = loader.get_template('familia/index.html')
  
    return HttpResponse(template.render(request))
