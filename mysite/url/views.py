from django.shortcuts import (render, render_to_response, 
							HttpResponse, HttpResponseRedirect)
from django.views.decorators.http import require_GET, require_POST
from django.template import RequestContext
from url.models import Url
import string
import random
#from url.forms import linksubmit
# Create your views here.


def index(request):	
	if request.method == 'GET':
		return render_to_response('index.html', {}, 
			               context_instance=RequestContext(request))

	if request.method == 'POST':
		url = request.POST['url']
		
		existing = Url.objects.filter(url=url)
		# Check if the url already exists in the database
		# return the saved hash instead of creating a new
		if len(existing) > 0:
			return HttpResponse('http://' + request.get_host() + '/' + 
								existing[0].short)
		
		# Create a random hash for the url, ideally it
		# should be short so that it shortens the url
		# ideal length set 5 over base62
		short = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxvyz') for i in range(5))
		u = Url(url=url, short=short)
		u.save()

		# Return the minified url
		return HttpResponse( 'http://' + request.get_host() + '/' +  u.short)

def redirect(request, uuid):
	url = Url.objects.get(short=uuid)
	return HttpResponseRedirect(url.url)
