from django.conf import settings 
from django.contrib import admin
from django.urls import path, include
from repository.views import homepage, about, author_create, add_category, add_venue, update_post
from django.conf.urls import url
from django import views as django_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('about/', about, name = 'about'),
    path('update_post/<slug>/', update_post, name='update_post'),
    path('author_create/', author_create, name='author_create'),
    path('add_category/', add_category, name='add_category'),
    path('add_venue/', add_venue, name='add_venue'),
    url(r'^jsi18n/$', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]