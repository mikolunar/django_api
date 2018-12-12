# posts/admin.py
from django.contrib import admin
from . models import Post
from . models import Car

admin.site.register(Post)
admin.site.register(Car)