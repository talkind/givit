from django.shortcuts import render
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']

        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
        user.save();

        return redirect('/')

    else:
        return render(request, 'register.html')