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
    context = {
        'post': post,
    }
    return render(request, 'single-post.html', context)