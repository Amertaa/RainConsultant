from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def Login(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'login.html')
    elif request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('posts')

        messages.error(request, 'Invalid username or password')
        return render(request, 'login.html', {'form': form})


def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
