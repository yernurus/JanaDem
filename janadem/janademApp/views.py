from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .forms import LoginForm, RegistrationForm
from .models import UserModel

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = UserModel.objects.filter(phone_number=phone_number).first()
            if user and check_password(password, user.password):
                # User authenticated, do something
                return redirect('success_url')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

def success(request):
    return render(request, 'user/success.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            name = form.cleaned_data['name']
            date_of_birth = form.cleaned_data['date_of_birth']
            password = form.cleaned_data['password']

            # Create user object
            user = UserModel.objects.create_user(phone_number=phone_number, name=name, date_of_birth=date_of_birth, password=password)
            
            # Redirect to a success page
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'user/registration.html', {'form': form})

def registration_success(request):
    return render(request, 'user/success.html')
