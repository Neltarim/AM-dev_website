from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Client, Company

def index(request):

    template = loader.get_template('mainapp/index.html')
    HttpResponse.status_code = 200
    return HttpResponse(template.render(request=request))

def thanks(request):
    template = loader.get_template('mainapp/thanks.html')
    HttpResponse.status_code = 201
    return HttpResponse(template.render(request=request))


def client_contact(request):
    template = None
    
    if request.method == 'POST':

        new_client = Company()

        new_client.last_name = request.POST.get('last_name')
        new_client.first_name = request.POST.get('first_name')
        new_client.email = request.POST.get('email')
        new_client.phone = request.POST.get('phone')
        new_client.message = request.POST.get('message')


        try :
            print("trying to save new entry ...")
            new_client.save()

        except:

            HttpResponse.status_code = 401
            print("oops. New entry failed.")
            template = loader.get_template('mainapp/form_client.html')
            return HttpResponse(template.render(request=request))

        print()
        print("NEW CLIENT ENTRY :")
        print("Name :" + new_client.first_name)
        print("Type :" + new_client.last_name)
        print("Email :" + new_client.email)
        print("Message :" + new_client.message)
        print()

        thx = loader.get_template('mainapp/thanks.html')
        HttpResponse.status_code = 201
        return HttpResponse(thx.render(request=request))

    else:
        template = loader.get_template('mainapp/form_client.html')
    
    return HttpResponse(template.render(request=request))

def hiring_contact(request):
    template = None
    
    if request.method == 'POST':

        new_company = Company()

        new_company.last_name = request.POST.get('last_name')
        new_company.first_name = request.POST.get('first_name')
        new_company.email = request.POST.get('email')
        new_company.phone = request.POST.get('phone')
        new_company.message = request.POST.get('message')


        try :
            print("trying to save new entry ...")
            new_company.save()

        except:

            HttpResponse.status_code = 401
            print("oops. New entry failed.")
            template = loader.get_template('mainapp/form_hiring.html')
            return HttpResponse(template.render(request=request))

        print()
        print("NEW COMPANY ENTRY :")
        print("Name :" + new_company.first_name)
        print("Type :" + new_company.last_name)
        print("Email :" + new_company.email)
        print("Message :" + new_company.message)
        print()

        thx = loader.get_template('mainapp/thanks.html')
        HttpResponse.status_code = 201
        return HttpResponse(thx.render(request=request))

    else:
        template = loader.get_template('mainapp/form_hiring.html')
    
    return HttpResponse(template.render(request=request))