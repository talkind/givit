from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from friendreq.models import ItemsFound, ItemRequest
from . models import CoordinatedItems, CoordinationForm, create_new_coordinations, close_related_request

def coordinator_create_view(request):
    if request.method == 'GET':
        form = CoordinationForm()
        matchedItems = ItemsFound.objects.filter(match=True)
        openRequests = ItemRequest.objects.filter(status='in_process')
        users = User.objects.all()
        
        return render (request, 'coordinator.html', {'form': form, 'matchedItems':matchedItems, 'openRequests':openRequests, 'users': users})
    else:
        form = CoordinationForm(request.POST or None)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.save()
            close_related_request(request);
        context = {
            'form' :form
        }
        return redirect('/coordinate')


        
