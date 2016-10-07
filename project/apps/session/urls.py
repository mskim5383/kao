from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', 'apps.session.views.user_login'),
    url(r'^logout/$', 'apps.session.views.user_logout'),
    url(r'^register/$', 'apps.session.views.register'),
    url(r'^$', 'apps.session.views.main'),
]
