from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required


from demo_data import views as demo_data_views

urlpatterns = [
	url(r'^$', login_required(demo_data_views.home), name='demo-data-home'),
	url(r'^category-(?P<category_num>[0-9]+)/$', 
		login_required(demo_data_views.category_page),
		name='category-page'),
	url(r'^category-(?P<category_num>[0-9]+)/review-(?P<review_num>[0-9]+)/$',
		login_required(demo_data_views.review_page),
		name='review-page'),
]