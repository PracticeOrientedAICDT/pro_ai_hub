import os
import yaml
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

from .models import Post, Author
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect


from .forms import PostForm, AuthorForm, VenueForm, CategoryForm, ArxivForm, NewUserForm
from .utils import generate_qmd_header, generate_page_content, create_push_request, generate_qmd_header_for_arxiv


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
            current_path = '/'.join(current_path.split('/')[:-1])
            current_path = current_path + f'/icr/content/{folder_name}/'

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
                'folder_name': folder_name,
                'form': filled_form
            }

        return render(request, 'repository/submission.html', context=context)

    else:
        filled_form = PostForm()
        return render(
            request,
            'repository/new_post.html',
            context={
                'form': filled_form})


def about(request):
    return render(request, 'repository/about_page.html')


def author_create(request):

    if request.method == 'GET':
        form = AuthorForm()
        context = {'form': form}
        return render(
            request,
            'repository/create_author.html',
            context=context)

    form = AuthorForm(request.POST)

    if form.is_valid():
        author_instance = form.save()
        instance = serializers.serialize('json', [author_instance, ])
        return JsonResponse({"instance": instance}, status=200)


def add_venue(request):

    if request.method == 'GET':
        form = VenueForm()
        context = {'form': form}
        return render(request, 'repository/add_venue.html', context=context)

    form = VenueForm(request.POST)

    if form.is_valid():
        venue_instance = form.save()
        instance = serializers.serialize('json', [venue_instance, ])
        return JsonResponse({"instance": instance}, status=200)


def add_category(request):

    if request.method == 'GET':
        form = CategoryForm()
        context = {'form': form}
        return render(request, 'repository/add_category.html', context=context)

    form = CategoryForm(request.POST)
    if form.is_valid():
        category_instance = form.save()
        instance = serializers.serialize('json', [category_instance, ])
        return JsonResponse({"instance": instance}, status=200)


def update_post(request, slug):

    context = {}

    post = get_object_or_404(Post, slug=slug)

    form = PostForm(request.POST or None, instance=post)

    print(post.slug)
    if request.method == 'GET':
        context = {'form': form}
        return render(request, "repository/update_post.html", context=context)

    if form.is_valid():
        post_instance = Post.objects.get(slug=slug)
        form = PostForm(request.POST, instance=post)
        form.save()
        instance = serializers.serialize('json', [post_instance, ])
        return JsonResponse({"instance": instance}, status=200)

    print(form.errors.as_data())


def arxiv_post(request):

    if request.method == 'POST':
        context = {}

        filled_form = ArxivForm(request.POST)

        if filled_form.is_valid():
            form_data = filled_form.cleaned_data

            url = form_data.get('link', '')
            soup = BeautifulSoup(requests.get(url).content, "html.parser")

            meta_tags = list(soup.find_all("meta"))
            tags = list(meta_tags)
            names = [
                'citation_author',
                'citation_abstract',
                'citation_title',
                'citation_pdf_url']
            selected_tags = [tag for tag in tags if tag.get('name') in names]

            data = defaultdict(list)

            for tag in selected_tags:
                if tag.get('name') == 'citation_author':
                    data[tag.get('name')].append(tag.get('content'))
                else:
                    data[tag.get('name')] = tag.get('content')

            content = generate_qmd_header_for_arxiv(data)

            folder_name = slugify(content.get('title', ''))

            current_path = os.getcwd()
            current_path = '/'.join(current_path.split('/')[:-1])
            current_path = current_path + f'/icr/content/{folder_name}/'
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
                'folder_name': folder_name,
                'form': filled_form
            }

        return render(request, 'repository/submission.html', context=context)

    else:
        form = ArxivForm()
        context = {
            'form': form
        }
        return render(request, 'repository/arxiv_post.html', context=context)


def email_check(user):
    if user.is_authenticated:
        return user.email.endswith('@bristol.ac.uk')
    print('Fudeu')
    return False


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            email = form_data['email']

            if email.endswith('@bristol.ac.uk'):
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successfull.")
                return redirect("/home")
            messages.error(
                request, "Email should belong to @bristol.ac.uk domain.")
            return render(
                request,
                'registration/register.html',
                context={
                    "register_form": form})
        messages.error(
            request,
            "Uncessfull registration. Invalid information.")
    form = NewUserForm()
    return render(
        request,
        'registration/register.html',
        context={
            "register_form": form})
