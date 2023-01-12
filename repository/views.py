import os
import yaml

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .models import Category, Post, Author
from django.http import JsonResponse
from django.core import serializers


from .forms import PostForm, AuthorForm, VenueForm, CategoryForm
from .utils import generate_qmd_header, generate_page_content, create_push_request

@login_required
def homepage(request):

    if request.method == 'POST':
        filled_form = PostForm(request.POST)

        if filled_form.is_valid():
            form_data = filled_form.cleaned_data 


            content = {}
            content = generate_qmd_header(content, form_data)

            folder_name = slugify(content.get('title', ''))

            current_path = os.getcwd()
            current_path = current_path+f'/icr/content/{folder_name}/'

            file_path = f'{current_path}index.qmd'

            if not os.path.exists(current_path):
                os.makedirs(current_path)

            with open(file_path, 'w+') as fp:
                fp.write('---\n')
                yaml.dump(content, fp)
                fp.write('\n---')

            generate_page_content(content, file_path)

            create_push_request(file_path, folder_name)

            context = {
                'folder_name':folder_name,
                'form': filled_form
            }

        return render(request, 'repository/submission.html', context=context)

    else:
        filled_form = PostForm()
        return render(request, 'repository/new_post.html', context={'form': filled_form})

def about(request):
    return render(request, 'repository/about_page.html')

def author_create(request):

    if request.method == 'GET':
        form  = AuthorForm()
        context={'form':form}
        return render(request, 'repository/create_author.html', context=context)
    
    form = AuthorForm(request.POST)

    if form.is_valid():
        author_instance = form.save()
        instance = serializers.serialize('json', [ author_instance, ])
        return JsonResponse({"instance": instance}, status=200)



def add_venue(request):

    if request.method == 'GET':
        form  = VenueForm()
        context={'form':form}
        return render(request, 'repository/add_venue.html', context=context)
    
    form = VenueForm(request.POST)

    if form.is_valid():
        venue_instance = form.save()
        instance = serializers.serialize('json', [ venue_instance, ])
        return JsonResponse({"instance": instance}, status=200)


def add_category(request):

    if request.method == 'GET':
        form  = CategoryForm()
        context = {'form':form}
        return render(request, 'repository/add_category.html', context=context)
        
    form = CategoryForm(request.POST)
    if form.is_valid():
        category_instance = form.save()
        instance = serializers.serialize('json', [ category_instance, ])
        return JsonResponse({"instance": instance}, status=200)
        

def update_post(request, slug):
    
    context = {}

    post = get_object_or_404(Post, slug = slug)

    form = PostForm(request.POST or None, instance = post)

    print(post.slug)
    if request.method == 'GET':
        context = {'form':form} 
        return render(request, "repository/update_post.html", context=context)

    
    if form.is_valid():
        post_instance = Post.objects.get(slug=slug)
        form = PostForm(request.POST, instance=post)
        form.save()
        instance = serializers.serialize('json', [ post_instance, ])
        return JsonResponse({"instance": instance}, status=200)
    
    print(form.errors.as_data())