from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def blog_homepage(request):
    if request.method == 'POST':
        filled_form = BlogPostForm(request.POST)
        
        print(filled_form.is_valid())
        if filled_form.is_valid():
            post_instance = filled_form.save()
            return redirect('/')

        
        return render(request, 'blog/new_blogpost.html', {'form': filled_form})
    else:
        filled_form = BlogPostForm()
        return render(request, 'blog/new_blogpost.html', context={'form': filled_form})