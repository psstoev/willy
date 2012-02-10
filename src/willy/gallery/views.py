# Create your views here.
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from willy.gallery.models import Category
from willy.gallery.forms import CategoryForm

def add_category(request):
    if request.method == 'GET':
        return render_to_response('add_category.html',
                                  {'form' : CategoryForm()},
                                  context_instance=RequestContext(request))
    form = CategoryForm(request.POST)
    if form.is_valid():
        category_data = form.cleaned_data
        category_data['owner'] = request.user
        
        category = Category(**category_data)
        category.save()
        return redirect('/welcome/')

def view_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render_to_response('category.html',
                              {'category' : category},
                              context_instance=RequestContext(request))
