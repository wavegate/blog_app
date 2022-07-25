from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')