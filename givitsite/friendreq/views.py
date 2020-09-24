from django.db import transaction
from django.shortcuts import render

from .forms import itemRequestForm
from .models import ItemRequest, ItemsFound


def itemRequest_create_view(request):
    form = itemRequestForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            fs = form.save(commit=False)
            fs.friend_id = request.user
            fs.save()
        context = {
            'form': form
        }
        return render(request, "demandDB.html", context)
    else:
        context = {
            'form': form
        }
        return render(request, 'itemRequestform.html', context)


def requestItem(request):
    # on match
    if request.method == 'POST':
        with transaction.atomic():
            item_id = request.POST["item_id"]
            ItemsFound.objects.filter(
                pk=item_id).update(match=True)
            req_id = request.POST["req_id"]
            ItemRequest.objects.filter(
                pk=req_id).update(status='in_process')

    founditems = ItemsFound.objects.all()
    allrequests = ItemRequest.objects.filter(status='open')
    context = {'founds': founditems, 'allRequests': allrequests}
    return render(request, 'feed.html', context)
