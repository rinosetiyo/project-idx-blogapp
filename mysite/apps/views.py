from django.shortcuts import render, get_object_or_404
from apps.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request,'index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    category_by_author = Post.objects.filter(author=post.author).order_by('-date_posted')
    post.view_count += 1
    post.save()
    context = {
        'post': post,
        'category_by_author': category_by_author,
    }
    return render(request, 'single-post.html', context)

def post_author(request):
    posts = Post.objects.filter(author=request.user).order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request, 'test.html' , context)