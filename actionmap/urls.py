from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all_addresses$', views.get_all_addresses_json, name='all_addresses$'),
    url(r'^save_address', views.save, name='save_address'),
]