from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^makechangeshere/', include(admin.site.urls)),
]
