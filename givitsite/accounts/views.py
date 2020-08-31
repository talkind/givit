from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
# from .models import Users

# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        date_of_birth = request.POST['date_of_birth']
        address_street = request.POST['address_street']
        address_home_number = request.POST['address_home_number']
        address_city = request.POST['address_city']
        phone_number = request.POST['phone_number']
        field_of_study = request.POST['field_of_study']
        degree = request.POST['degree']
        current_year = request.POST['current_year']
        scholarship = request.POST['scholarship']
        type_of_friendship = request.POST['type_of_friendship']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email = email, password = password1, first_name = first_name, last_name = last_name, address_street = address_street, date_of_birth = date_of_birth, address_home_number = address_home_number, address_city = address_city, phone_number = phone_number, field_of_study = field_of_study, degree = degree, current_year = current_year, scholarship = scholarship, type_of_friendship = type_of_friendship)
                user.save();
                return redirect('home.html')
        else:
            messages.info(request,'password not match')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

