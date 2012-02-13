# Create your views here.
import os, glob
import hashlib
from datetime import datetime

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.core.files import File
from django.conf import settings

from willy.gallery.models import Category, Picture
from willy.gallery.forms import CategoryForm, PictureUploadForm, PictureEditForm

def get_categories(request):
    if request.user.is_authenticated():
        categories = Category.objects.filter(owner=request.user)
    else:
        categories = Category.objects.all()[:10]
        
    return categories

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
    categories = get_categories(request)
    category = get_object_or_404(Category, pk=category_id)
    subcategories = Category.objects.filter(category_parent=category)
    pictures = Picture.objects.filter(category=category)
    return render_to_response('view_category.html',
                              {'user' : request.user,
                              'cat' : category,
                              'cat_id' : int(category_id),
                              'categories' : categories,
                              'subcategories' : subcategories,
                              'pictures' : pictures,
                              },
                              context_instance=RequestContext(request))

@login_required                              
def upload_picture(request):
    if request.method == 'GET':
        return render_to_response('upload_picture.html',
                                  {'form' : PictureUploadForm(user=request.user)},
                                  context_instance=RequestContext(request))

    
    form = PictureUploadForm(request.POST, request.FILES)

    if form.is_valid():
        picture_data = {}
        picture_data['name'] = form.cleaned_data['name']
        picture_data['description'] = form.cleaned_data['description']
        picture_data['owner'] = request.user
        picture_data['uploaded'] = datetime.now()

        # Generate unique name
        uploaded_file = request.FILES['pic']
        message = '_'.join([request.user.username, uploaded_file.name, str(datetime.now())])
        extension = uploaded_file.name.split('.')[-1]
        request.FILES['pic'].name = hashlib.sha1(message).hexdigest() + '.' + extension
        picture_data['pic'] = File(request.FILES['pic'])

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
    categories = get_categories(request)
    picture = get_object_or_404(Picture, pk=picture_id)
    return render_to_response('view_picture.html',
                              {'picture' : picture},
                              context_instance=RequestContext(request))

@login_required
def edit_picture(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    if picture.owner != request.user:
        return render_to_response('gallery_error.html',
                                  {'message' : _("You don't have enough privileges to edit this picture")},
                                  context_instance=RequestContext(request))
    if request.method == 'GET':
        return render_to_response('edit_picture.html',
                                  {'form' : PictureEditForm(instance=picture),
                                   'picture_id' : picture_id},
                                  context_instance=RequestContext(request))

    form = PictureEditForm(request.POST)
    if form.is_valid():
        picture_data = form.cleaned_data

        picture.name = form.cleaned_data['name']
        picture.description = form.cleaned_data['description']
        for category in form.cleaned_data['category']:
            picture.category.add(category)
        picture.save()
        
        return redirect('/session/welcome/')

    return render_to_response('edit_picture.html',
                              {'form' : form,
                               'picture_id' : picture_id},
                              context_instance=RequestContext(request))

@login_required
def delete_picture(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    if picture.owner != request.user:
        return render_to_response('gallery_error.html',
                                  {'message' : _("You don't have enough privileges to delete this category")},
                                  context_instance=RequestContext(request))

    name = os.path.join(settings.MEDIA_ROOT, '.'.join(picture.pic.name.split('.')[:-1]))
    for filename in glob.glob(name + '*'):
        os.remove(filename)
    picture.delete()

    return redirect('/session/welcome/')
                              
def view_categories(request):
    categories = get_categories(request)
    all_categories = Category.objects.all()
    subcat_count = [len(Category.objects.filter(category_parent=category)) for category in Category.objects.all()]
    picture_count = [len(Picture.objects.filter(category=category)) for category in Category.objects.all()]
    cat_info = zip(all_categories, subcat_count, picture_count)
    if request.method == 'GET':
        return render_to_response('view_categories.html',
                                  {'user' : request.user,
                                  'categories' : categories,
                                  'cat_info' : cat_info
                                  },
                                  context_instance=RequestContext(request))
                                  
def view_pictures(request):
    categories = get_categories(request)
    pictures = Picture.objects.all()
    if request.method == 'GET':
        return render_to_response('view_pictures.html',
                                  {'user' : request.user,
                                  'pictures' : pictures,
                                  'categories' : categories
                                  },
                                  context_instance=RequestContext(request))
