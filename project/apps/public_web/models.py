from django.db import models

from kao.settings import UPLOAD_DIR

# Create your models here.
class WebContent(models.Model):
    name = models.CharField(max_length=20, null=False, default='')
    content = models.TextField()

    def __str__(self):
        return '%s' % (self.name)

class ConcertContent(models.Model):
    name = models.CharField(max_length=20, null=False, default='')
    content = models.TextField()
    poster = models.ImageField(null=True, blank=True, upload_to=UPLOAD_DIR)

    def poster_url(self):
        if self.poster:
            return '/upload/'+self.poster.url.split('/')[-1]
        return '/media/img/poster.jpg'
