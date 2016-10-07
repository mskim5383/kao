from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from apps.session.models import UserProfile
from apps.session.forms import UserForm, UserProfileForm

def main(request):
    return render(request, 'session/main.html')

def user_login(request):
    if request.user.is_authenticated():
        return redirect('/main')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            next_url = request.POST.get('next', '/main')
            if next_url == '':
                next_url = '/main'
            return redirect(next_url)
        else:
            return render(request, 'session/login.html',
                          {'error': 'Invalid login',
                           'next': request.POST.get('next', '/')})
    return render(request, 'session/login.html',
                    {'next': request.GET.get('next', '/')})

def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('/session/login')

def register(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        user_form = UserForm(request.POST, repassword=request.POST.get('repassword', ''))
        user_profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            userprofile = user_profile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('/main')
    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()
    return render(request, 'session/register.html',
                    {'user_form': user_form,
                     'user_profile_form': user_profile_form})
