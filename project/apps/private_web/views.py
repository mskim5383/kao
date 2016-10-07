from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from apps.private_web.models import BoardComment


@login_required(login_url='/session/login/')
def board(request):
    if request.method == 'POST':
        userprofile = request.user.userprofile
        content = request.POST.get('content', '')
        board_comment = BoardComment()
        board_comment.userprofile = userprofile
        board_comment.content = content
        board_comment.save()
    board_comment_list = BoardComment.objects.all()
    return render(request, 'private_web/board.html',
            {'board_comment_list': board_comment_list})
