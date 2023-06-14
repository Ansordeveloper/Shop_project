from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'new.html'
    fields = ['title', 'author', 'text']
    success_url = reverse_lazy('home')

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('home')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home') 