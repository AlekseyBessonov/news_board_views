from django.contrib import admin
from .models import Post, Category, Comment, Author
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
