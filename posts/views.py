from rest_framework import generics
from . models import Post
from .serializers import PostSerializer


from django.shortcuts import render
from django.forms import BaseForm

# from django.contrib.auth.decorators import login_required

from . forms import PostForm

from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def post(request):

    form = PostForm()
    test = 'TEST'
    return render(request, 'posts/post.html', {'form': test})
# Create your views here.
