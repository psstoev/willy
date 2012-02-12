# Create your views here.
from datetime import datetime

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

from willy.gallery.models import Category, Picture
from willy.gallery.forms import CategoryForm, PictureUploadForm

@login_required
def add_category(request):
    if request.method == 'GET':
        return render_to_response('add_category.html',
                                  {'form' : CategoryForm(user=request.user)},
                                  context_instance=RequestContext(request))

    form = CategoryForm(request.POST)
    if form.is_valid():
        category_data = form.cleaned_data
        category_data['owner'] = request.user
        
        category = Category(**category_data)
        category.save()
        return redirect('/session/welcome/')

    return render_to_response('add_category.html',
                              {'form' : form},
                              context_instance=RequestContext(request))

@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if category.owner != request.user:
        return render_to_response('gallery_error.html',
                                  {'message' : _("You don't have enough privileges to edit this category")},
                                  context_instance=RequestContext(request))
    if category.name == category.owner.username:
        return render_to_response('gallery_error.html',
                                  {'message' : _("You can't edit this category")},
                                  context_instance=RequestContext(request))
    if request.method == 'GET':
        return render_to_response('edit_category.html',
                                  {'form' : CategoryForm(instance=category),
                                   'category_id' : category_id},
                                  context_instance=RequestContext(request))

    form = CategoryForm(request.POST)
    if form.is_valid():
        category_data = form.cleaned_data
        
        category.category_parent = category_data['category_parent']
        category.name = category_data['name']
        category.save()
        return redirect('/session/welcome/')

    return render_to_response('edit_category.html',
                              {'form' : form,
                               'category_id' : category_id},
                              context_instance=RequestContext(request))

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if category.owner != request.user:
        return render_to_response('gallery_error.html',
                                  {'message' : _("You don't have enough privileges to delete this category")},
                                  context_instance=RequestContext(request))
    if category.name == category.owner.username:
        return render_to_response('gallery_error.html',
                                  {'message' : _("You can't delete this category")},
                                  context_instance=RequestContext(request))

    category.delete()
    return redirect('/session/welcome/')

def view_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render_to_response('category.html',
                              {'category' : category},
                              context_instance=RequestContext(request))
                              
def upload_picture(request):
    if request.method == 'GET':
        return render_to_response('upload_picture.html',
                                  {'form' : PictureUploadForm()},
                                  context_instance=RequestContext(request))

    form = PictureUploadForm(request.POST)
    if form.is_valid():
        picture_data = {}
        picture_data['name'] = form.cleaned_data['name']
        picture_data['description'] = form.cleaned_data['description']
        picture_data['owner'] = request.user
        picture_data['uploaded'] = datetime.now()

        picture = Picture(**picture_data)
        picture.save()
        
        for category in form.cleaned_data['category']:
            picture.category.add(category)
        picture.save()
        
        return redirect('/session/welcome/')

    return render_to_response('upload_picture.html',
                              {'form' : form},
                              context_instance=RequestContext(request))
                              
def view_picture(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    return render_to_response('view_picture.html',
                              {'picture' : picture},
                              context_instance=RequestContext(request))
