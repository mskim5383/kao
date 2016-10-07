from django.db import models

# Create your models here.
class WebContent(models.Model):
    name = models.CharField(max_length=20, null=False, default='')
    content = models.TextField()

    def __str__(self):
        return '%s' % (self.name)
