from django.shortcuts import render

def entrance(request):
    return render(request, 'public_web/entrance.html')

def main(request):
    return render(request, 'public_web/main.html')

def about(request):
    return render(request, 'public_web/about.html')

def concert(request):
    return render(request, 'public_web/concert.html')

def media(request):
    return render(request, 'public_web/media.html')

def board(request):
    return render(request, 'public_web/board.html')

def contact(request):
    return render(request, 'public_web/contact.html')
