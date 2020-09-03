from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from . import views

app_name = 'video'


urlpatterns = [
	url(r'^(?P<no>)$', views.Videos.as_view()),
	url(r'^(?P<no>).html$', views.Compatible.as_view()),
]
