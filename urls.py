from django.conf.urls import include, url
from django.contrib import admin

import scrapes.views as scrapes_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', scrapes_views.home, name='home'),
]
