from django.shortcuts import render
from django.http import HttpResponse

from apps.public_web.models import WebContent

import json

def entrance(request):
    model_dict = _model_load('entrance')
    return render(request, 'public_web/entrance.html', model_dict)

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

def webcontent(request):
    result = {'status': 'fail'}
    if request.user.is_staff and request.method == 'POST':
        name = request.POST.get('name', '')
        content = request.POST.get('content', '')
        if name != '':
            web_content = _model_save(name, content)
            result['status'] = 'success'
            result['content'] = web_content.content
    return HttpResponse(json.dumps(result), content_type='application/json')


def _model_load(*args):
    model_dict = {}
    for model_name in args:
        try:
            web_content = WebContent.objects.get(name=model_name)
        except:
            web_content = WebContent()
            web_content.name = model_name
            web_content.save()
        model_dict[model_name] = web_content
    return model_dict

def _model_save(model_name, content):
    try:
        web_content = WebContent.objects.get(name=model_name)
    except:
        web_content = WebContent()
        web_content.name = model_name
    web_content.content = content
    web_content.save()
    return web_content
