from django.contrib import admin
from .models import Author, Category, Post, Venue, Conference



admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Conference)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ("authors", "venue", "categories",)


admin.site.register(Venue)