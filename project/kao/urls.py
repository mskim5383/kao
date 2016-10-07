from django.conf.urls import include, url
from django.contrib import admin

from kao.settings import BASE_DIR

import os

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^session/', include('apps.session.urls')),
    url(r'^private_web/', include('apps.private_web.urls')),

    # Upload Root
    url(r'^upload/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(BASE_DIR, 'upload')}),

    url(r'^', include('apps.public_web.urls')),
]
