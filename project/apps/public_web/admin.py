from django.contrib import admin
from apps.public_web.models import WebContent, ConcertContent

# Register your models here.
admin.site.register(WebContent)
admin.site.register(ConcertContent)
