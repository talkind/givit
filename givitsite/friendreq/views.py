from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemRequest

# Create your views here.

def request(request):
    return render(request, 'request.html')

def itemrequest(request):
    city_val = request.POST["city"]
    item_val = request.POST["item"]
    special_val = request.POST["specialreq"]
    req = ItemRequest()
    req.item = item_val
    req.city = city_val
    req.special_req = special_val
    return render(request, 'demandDB.html',{'request':req})