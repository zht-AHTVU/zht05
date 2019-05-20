from django.conf.urls import url
from book import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^login$',views.login),
    url(r'^login_check$',views.login_check),
    url(r'^areas$',views.areas),
    url(r'^prov$', views.prov),
    url(r'^city(\d+)$', views.city),
    url(r'^dis(\d+)$',views.city)
]