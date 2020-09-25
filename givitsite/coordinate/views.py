from accounts.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from friendreq.models import ItemRequest, ItemsFound, REGION_CHOICES, ITEM_CHOICES
from .models import CoordinationForm, close_related_request


def coordinator_create_view(request):
    if request.method == 'GET':
        form = CoordinationForm()
        matchedItems, openRequests = get_data_query_sets(request)
        item_choices_list, region_choices_list = get_filters_as_lists()

        return render(request, 'coordinator.html',{'form': form, 'matchedItems': matchedItems, 'openRequests': openRequests, 'region_choices': region_choices_list, 'item_choices': item_choices_list})   
    else:
        form = CoordinationForm(request.POST or None)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.save()
            close_related_request(request)

        return redirect('/coordinate')

#Convert the tupple list to a string list so it can be rendered in the template
def get_filters_as_lists():
        item_choices_list = [] 
        region_choices_list = []

        for region in REGION_CHOICES: 
            region_choices_list.append(region[1])
        for item in ITEM_CHOICES:
            item_choices_list.append(item[1])
        return item_choices_list, region_choices_list
   
def get_data_query_sets(request):

    matchedItems = ItemsFound.objects.filter(match=True)
    openRequests = ItemRequest.objects.filter(status='in_process')

    item_filter = request.GET.get('item')
    pickup_city_filter = request.GET.get('city_pickup')

    if item_filter is not None and item_filter != "":
            matchedItems = matchedItems.filter(title = item_filter)
    if pickup_city_filter is not None and pickup_city_filter  != "":
        matchedItems = matchedItems.filter(city = pickup_city_filter)

    return matchedItems, openRequests
