from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)


def home(request):

	return HttpResponse('this is the homepage')
