# Create your views here.
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from willy.gallery.models import Category

def add_category(request):
    pass

def view_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render_to_response('category.html',
                              {'category' : category},
                              context_instance=RequestContext(request))
