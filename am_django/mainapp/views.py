from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Client, Company

def index(request):

    template = loader.get_template('mainapp/index.html')
    HttpResponse.status_code = 200
    return HttpResponse(template.render(request=request))


def client_contact(request):
    template = loader.get_template('mainapp/form_client.html')
    
    if request.method == 'POST':

        new_client = Client()
        
        new_client.first_name = request.POST.get('firstName')
        new_client.last_name = request.POST.get('lastName')
        new_client.email = request.POST.get('email')
        new_client.phone = request.POST.get('phone')
        new_client.message = request.POST.get('message')

        print("new entry")

        for key, value in request.POST.items():
            print('key: %s' % (key))
            print('value: %s' % (value))
        try :
            new_client.save()

        except:
            HttpResponse.status_code = 401
            template = loader.get_template('mainapp/index.html')
            return HttpResponse(template.render(request=request))

        print("NEW ENTRY :")
        print("Name :" + new_client.first_name)
        print("Type :" + new_client.last_name)
        print("Email :" + new_client.email)
        print("Message :" + new_client.message)

        template = loader.get_template('form/thanks.html')
        HttpResponse.status_code = 201

    return HttpResponse(template.render(request=request))

def hiring_contact(request):
    template = loader.get_template('mainapp/form_hiring.html')
    
    if request.method == 'POST':

        new_company = Client()

        print(request.POST)

        new_company.last_name = request.POST.get('last_name')
        new_company.first_name = request.POST.get('first_name')
        new_company.email = request.POST.get('email')
        new_company.phone = request.POST.get('phone')
        new_company.message = request.POST.get('message')

        try :
            new_company.save()

        except:
            HttpResponse.status_code = 401
            template = loader.get_template('mainapp/form_hiring.html')
            return HttpResponse(template.render(request=request))

        print("NEW ENTRY :")
        print("Name :" + new_company.first_name)
        print("Type :" + new_company.last_name)
        print("Email :" + new_company.email)
        print("Message :" + new_company.message)

        template = loader.get_template('mainapp/thanks.html')
        HttpResponse.status_code = 201

    return HttpResponse(template.render(request=request))