from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

'''
Create a DetailView class.
in this view we define the model we are using, Post, and the template we want to associate with, post.detail.html
by Defaul DetailView provides a context object we can use in our template, called object or the name of our 
model in lowercase. ( in this case it is : post)
'''


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


'''
Create a view for adding post, in this case we use a generic class CreateVIew
'''


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__' # this refers to the field of the model (database)
