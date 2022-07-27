from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','body']

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','body']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts')