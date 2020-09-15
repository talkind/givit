from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Profile
from django.contrib.auth.models import User
from django.conf import settings

def home(request):

    if request.user.is_authenticated:
        user_profile = Profile.objects.get(user = request.user)
        return render(request, 'home.html', {'user_profile': user_profile})
    else:
        return render(request, 'home.html')
