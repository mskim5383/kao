from django.conf.urls import include, url

urlpatterns = [
    url(r'^main/$', 'apps.public_web.views.main'),
    url(r'^about/$', 'apps.public_web.views.about'),
    url(r'^concert/$', 'apps.public_web.views.concert'),
    url(r'^media/$', 'apps.public_web.views.media'),
    url(r'^board/$', 'apps.public_web.views.main'),
    url(r'^contact/$', 'apps.public_web.views.contact'),
    url(r'^$', 'apps.public_web.views.entrance'),
]
