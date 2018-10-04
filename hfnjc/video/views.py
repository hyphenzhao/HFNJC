# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponseRedirect

class Videos(APIView):
	def get(self, request, no):
		context = {
			"no": no
		}
		return render(request, "videos.html", context)
class Compatible(APIView):
	def get(self, request, no):
		return HttpResponseRedirect("/video/" + no)



# Create your views here.
