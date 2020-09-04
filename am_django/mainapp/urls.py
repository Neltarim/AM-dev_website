from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^client_contact/', views.client_contact, name='client_contact'),
]