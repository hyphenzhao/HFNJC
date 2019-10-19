from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'yikai'

urlpatterns = [
	url(r'^index/$', TemplateView.as_view(template_name="yikai/index.html")),
	# url(r'^index/$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
