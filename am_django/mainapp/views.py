from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.mail import send_mail
from os import getcwd
from os.path import isfile
import json

from .models import Client, Company

def index(request):
    """Main view index"""
    template = loader.get_template('mainapp/index.html')
    HttpResponse.status_code = 200
    return HttpResponse(template.render(request=request))

def thanks(request):
    """Thanks view"""
    template = loader.get_template('mainapp/thanks.html')
    HttpResponse.status_code = 201
    return HttpResponse(template.render(request=request))

def easy_antispam(request):
    """Store anonymous ips to prevent spamming and cancel requests."""
    x_forward_for =  request.META.get('HTTP_X_FORWARDED_FOR')

    new_ip = ''

    if x_forward_for:
        new_ip = x_forward_for.split(',')[0]
    else:
        new_ip = request.META.get('REMOTE_ADDR')

    ano_ips_path = getcwd() + "/mainapp/easy_antispam/ips.json"

    with open(ano_ips_path, 'r') as file:
        ano_ips = json.load(file)

    for ip in ano_ips :
        if ip == new_ip:
            return False

    ano_ips.append(new_ip)

    with open(ano_ips_path, 'w') as file:
        json.dump(ano_ips, file, indent=4, separators=(',', ': '))

    return True

def client_contact(request):
    """Client form view"""
    template = None
    
    if request.method == 'POST':
        if easy_antispam(request): #if the ip is new

            new_client = Client()

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
            HttpResponse.status_code = 401
            template = loader.get_template('mainapp/index.html')

    else:
        template = loader.get_template('mainapp/form_client.html')
    
    return HttpResponse(template.render(request=request))

def hiring_contact(request):
    """Company form view"""
    template = None
    
    if request.method == 'POST':

        if easy_antispam(request): #if the ip is new
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
            print("Last name :" + new_company.last_name)
            print("Email :" + new_company.email)
            print("Message :" + new_company.message)
            print()

            adm_msg = 'Name:{} {}\nEmail:{}\nPhone:{}\nMessage:{}'.format(new_company.last_name, new_company.first_name, new_company.email, new_company.phone, new_company.message)
            send_mail(
                'New Company Entry',
                adm_msg,
                'noreply@am_web.fr',
                ['am.devpro@gmail.com'],
                fail_silently=True
            )

            thx = loader.get_template('mainapp/thanks.html')
            HttpResponse.status_code = 201
            return HttpResponse(thx.render(request=request))
        
        else:
            HttpResponse.status_code = 401
            template = loader.get_template('mainapp/index.html')

    else:
        template = loader.get_template('mainapp/form_hiring.html')
    
    return HttpResponse(template.render(request=request))