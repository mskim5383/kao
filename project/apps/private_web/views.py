from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


@login_required(login_url='/session/login/')
def board(request):
    return render(request, 'private_web/board.html')
