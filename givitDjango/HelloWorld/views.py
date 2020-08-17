from django.shortcuts import render
from django.http import HttpResponse

def helloFun(request):
	return HttpResponse("Hello World\n first GIVIT project page!")

# Create your views here.
