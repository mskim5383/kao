from django.db import models

from kao.settings import UPLOAD_DIR

# Create your models here.
class BoardComment(models.Model):
    userprofile = models.ForeignKey('session.UserProfile',
            related_name='board_comment')
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
