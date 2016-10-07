from django.shortcuts import render

def main(request):
    return render(request, 'session/main.html')

def login(request):
    return render(request, 'session/login.html')

def logout(request):
    return render(request, 'session/logout.html')

def register(request):
    return render(request, 'session/register.html')
