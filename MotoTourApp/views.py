from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.views.generic import ListView, DetailView


# Index
class IndexView(ListView):
    template_name='MotoTourApp/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.all()


# Detail
class PostDetailView(DetailView):
    model=Post
    template_name = 'MotoTourApp/post-detail.html'
