from django.shortcuts import render
import json
from rest_framework.views import APIView
from django.http import HttpResponse

class ServerIP(APIView):
	def get(self, request):
		response_data = {
			"server_ip":  "192.168.137.1" 
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")

