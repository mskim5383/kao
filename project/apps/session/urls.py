from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', 'apps.session.views.login'),
    url(r'^logout/$', 'apps.session.views.logout'),
    url(r'^register/$', 'apps.session.views.register'),
    url(r'^$', 'apps.session.views.main'),
]
