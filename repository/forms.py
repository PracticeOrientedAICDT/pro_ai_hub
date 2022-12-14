from django import forms
from .models import Post, Author, Venue, Category

from django.contrib.admin import widgets

class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    overview = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    authors = forms.ModelMultipleChoiceField(
                    queryset=Author.objects.all(),
                    widget = forms.SelectMultiple(attrs={'class': 'form-control'})
                    )
    categories = forms.ModelMultipleChoiceField(
                    queryset=Category.objects.all(),
                    widget = forms.SelectMultiple(attrs={'class': 'form-control'})
                    )
    venue = forms.ModelMultipleChoiceField(
                    queryset=Venue.objects.all(),
                    widget = forms.SelectMultiple(attrs={'class': 'form-control'})
                    )
    citation = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pdf = forms.URLField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    supplement = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    slides = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    poster = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    code = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    video = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title',
                  'overview',
                  'authors',
                  'thumbnail',
                  'categories',
                  'venue',
                  'citation',
                  'pdf',
                  'supplement',
                  'slides',
                  'poster',
                  'code',
                  'video']

        labels = {'title': 'Title',
                  'overview' : 'TLDR',
                  'authors': 'Authors',
                  'thumbnail': 'Image',
                  'categories': 'Categories',
                  'venue': 'Venue',
                  'citation' : 'Citation',
                  'pdf' : 'Pdf Link',
                  'supplement': 'Supplement',
                  'slides' : 'Slides',
                  'poster' : 'Poster',
                  'code' : 'Code',
                  'video' : 'Video' }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['user', 'user_url']
        labels = ['name', 'url']

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['venue_name', 'year', 'venue_url']
        labels = ['Name', 'Year', 'URL']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = ['Title', 'Subtitle', 'Slug']