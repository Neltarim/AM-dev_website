from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    template = loader.get_template('mainapp/index.html')
    HttpResponse.status_code = 200
    return HttpResponse(template.render(request=request))