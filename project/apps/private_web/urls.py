from django.conf.urls import include, url

urlpatterns = [
    url(r'^board/', 'apps.private_web.views.board'),
]
