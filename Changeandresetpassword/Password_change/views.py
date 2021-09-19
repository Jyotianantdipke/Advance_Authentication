from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import UserForm
from django.shortcuts import render

# Create your views here.


def register_view(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'Password_change/register.html'
    context = {'form': form}
    return render(request, template_name, context)


def login_view(request):
    if request.method == 'POST':
        unm = request.POST.get('un')
        pswd = request.POST.get('pw')
        user = authenticate(username=unm, password=pswd)
        if user is not None:
            login(request, user)
            return redirect('show')
        else:
            messages.error(request, 'Invalid Credentials')
    template_name = 'Password_change/login.html'
    context = {}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('login')


def change_pass_view(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Updated Successfully')
            return redirect('show')
        else:
            messages.error(request, 'Check the fields')

    template_name = 'Password_change/changepassword.html'
    context = {'form': form}
    return render(request, template_name, context)



def home_view(request):
    template_name='Password_change/home.html'
    return render(request, template_name)


def show_view(request):
    template_name = 'Password_change/show.html'
    return render(request, template_name)
