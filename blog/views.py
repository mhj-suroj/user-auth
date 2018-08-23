from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .forms import RegisterForm, EditProfileForm
from django.contrib import messages



def home(request):
    return render(request, 'blog/home.html', {})

def profile(request):
    return render(request, 'blog/profile.html', {})

def user_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            messages.success(request, 'Congratulation! You have been logged in successfully.')
            return redirect('home')
        else:
            messages.success(request, 'Error logging in! Please try again.')
            return redirect('login')
    return render(request, 'blog/login.html', {})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'])
            messages.success(request, 'You have registered successfully.')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form':form})


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have edited your profile.')
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'blog/edit_profile.html', {'form':form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You have changed your password.')
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'blog/change_password.html', {'form':form})








