from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Author, Tag, Category, Post
from django.http import HttpResponseNotFound,Http404


def post_list(request):
    posts = get_list_or_404(Post.objects.order_by('-id'))
    context={'posts': posts}
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk, slug):
    post = get_object_or_404(Post,pk=pk)
    context = {'post' : post}
    return render(request, 'blog/post_detail.html', context)

def post_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = get_list_or_404(Post.objects.order_by('-id'), category=category)
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/post_by_category.html', context)

def post_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = get_list_or_404(Post.objects.order_by('-id'), tags=tag)
    context = {
        'tags': tag,
        'posts': posts,
    }
    return render(request, 'blog/post_by_tag.html', context)