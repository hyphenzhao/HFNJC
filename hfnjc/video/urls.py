from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from . import views

app_name = 'video'


urlpatterns = [
	url(r'^(?P<no>[0-9]+)$', views.Videos.as_view()),
	url(r'^(?P<no>[0-9]+).html$', views.Compatible.as_view()),
]
