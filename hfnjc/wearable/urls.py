from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from . import views

app_name = 'wearable'


urlpatterns = [
	url(r'^get_server_ip/$', views.ServerIP.as_view())
]
