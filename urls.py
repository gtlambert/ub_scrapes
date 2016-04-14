from django.conf.urls import include, url
from django.contrib import admin

import testapp.views as views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin', include(admin.site.urls)),
    url(r'test', views.home),
]
