from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Category, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'update_time', 'category', 'author']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
