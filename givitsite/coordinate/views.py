from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from friendreq.models import ItemsFound, ItemRequest
from . models import CoordinatedItems, CoordinationForm

def coordinator_create_view(request):
    if request.method == 'GET':
        form = CoordinationForm()
        matchedItems = ItemsFound.objects.filter(match=True)
        openRequests = ItemRequest.objects.filter(status='open')
        users = User.objects.all()
        
        # TODO - render a coordinator page with the above querySets
        return HttpResponse('This will be a coordinator page')
        
