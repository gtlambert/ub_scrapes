from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

import scrapes.views as scrapes_views

import demo_data.urls as demo_data_urls

urlpatterns = [
    url(r'^admin/',
        include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^makechangeshere/', include(admin.site.urls)),

    # HOME
    url(r'^$', login_required(scrapes_views.home), name='home'),

    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/logout/$', auth_views.logout,
        {'next_page': 'home'}, name='logout'),

    # DEMO_DATA
    url(r'^demo-data/', include(demo_data_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
