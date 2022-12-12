from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Category, Post, Author
from django.forms import formset_factory
from .forms import PostForm, AuthorForm, VenueForm, CategoryForm

from django.http import JsonResponse

from django.core import serializers

from django_addanother.views import CreatePopupMixin

def homepage(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by('-timestamp')
    context = {
        'posts' : posts,
        'categories' : categories
    }

    return render(request, 'repository/homepage.html', context)

def post(request, slug):
    post = Post.objects.get(slug = slug)
    context = {
        'post' : post
    }

    return render(request, 'repository/post.html', context)

def about(request):
    return render(request, 'repository/about_page.html')

def category_post_list(request, slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories_in=[category])
    context = {
        'post': posts
    }
    return render(request, 'repository/post_list.html', context)

def allposts(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'repository/all_posts.html', context)

def new_post(request):

    if request.method == 'POST':
        filled_form = PostForm(request.POST)
        
        print(filled_form.is_valid())
        if filled_form.is_valid():
            post_instance = filled_form.save()
            return redirect('/')

        
        return render(request, 'repository/new_post.html', {'form': filled_form})
    else:
        filled_form = PostForm()
        return render(request, 'repository/new_post.html', context={'form': filled_form})

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
    
    form = AuthorForm(request.POST)

    if form.is_valid():
        venue_instance = form.save()
        instance = serializers.serialize('json', [ venue_instance, ])
        return JsonResponse({"instance": instance}, status=200)


def add_category(request):

    if request.method == 'GET':
        form  = CategoryForm()
        context={'form':form}
        return render(request, 'repository/add_category.html', context=context)
    
    form = AuthorForm(request.POST)

    if form.is_valid():
        category_instance = form.save()
        instance = serializers.serialize('json', [ category_instance, ])
        return JsonResponse({"instance": instance}, status=200)

def update_post(request, slug):
    
    context = {}

    post = get_object_or_404(Post, slug = slug)

    form = PostForm(request.POST or None, instance = post)

    if form.is_valid():
        form.save()
        post_instance = form.save()
        instance = serializers.serialize('json', [ post_instance, ])
        JsonResponse({"instance": instance}, status=200)
    
    context["form"] = form

    return render(request, "repository/update_post.html", context)