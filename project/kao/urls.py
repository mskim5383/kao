from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^session/', include('apps.session.urls')),
    url(r'^', include('apps.public_web.urls')),
]
