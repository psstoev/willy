from django.shortcuts import render_to_response
from django.template import RequestContext

def welcome(request):
    return render_to_response('welcome.html',
                              {'user' : request.user},
                              context_instance=RequestContext(request))
