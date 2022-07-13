from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_list.html'
                  
    
class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'