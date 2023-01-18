from django.conf import settings 
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django import views as django_views

from blog.views import blog_homepage
from repository.views import homepage, about, author_create, add_category, add_venue, update_post, arxiv_post, register_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('about/', about, name = 'about'),
    path('update_post/<slug>/', update_post, name='update_post'),
    path('author_create/', author_create, name='author_create'),
    path('add_category/', add_category, name='add_category'),
    path('add_venue/', add_venue, name='add_venue'),
    path('blog/', blog_homepage, name='blog_homepage'),
    path('arxiv_post/', arxiv_post, name='arxiv_post'),
    path('register/', register_request, name='register'),
    url(r'^jsi18n/$', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]