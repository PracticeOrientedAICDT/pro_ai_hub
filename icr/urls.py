from django.conf import settings 
from django.contrib import admin
from django.urls import path
from repository.views import homepage, post, about, category_post_list, allposts, new_post, author_create, add_category, add_venue, update_post
from blog.views import blog_homepage, blogpost, new_blogpost
from django.conf.urls import url
from django import views as django_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about, name = 'about'),
    path('postlist/<slug>/', category_post_list, name = 'category_post_list'),
    path('posts', allposts, name = 'allposts'),
    path('update_post/<slug>/', update_post, name='update_post'),
    path('new_post', new_post, name='new_post'),
    path('new_blogpost', new_blogpost, name='new_blogpost'),
    path('author_create/', author_create, name='author_create'),
    path('add_category/', add_category, name='add_category'),
    path('add_venue/', add_venue, name='add_venue'),
    path('blog_homepage/', blog_homepage, name='blog_homepage'),
    path('blogpost/<slug>', blogpost, name='blogpost'),
    url(r'^jsi18n/$', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),
]
