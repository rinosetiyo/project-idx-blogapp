from django.shortcuts import render, get_object_or_404
from apps.models import Post
from apps.forms import CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request,'index.html', context)

def post_detail(request, slug):
    comment_form = CommentForm()
    post = get_object_or_404(Post, slug=slug)
    category_by_author = Post.objects.filter(author=post.author).order_by('-date_posted')
    post.view_count += 1
    post.save()

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            postid = request.POST.get("post_id")
            post = Post.objects.get(id=postid)
            comment.post = post
            comment.save()

    context = {
        'post': post,
        'category_by_author': category_by_author,
        'comment_form': comment_form,
    }
    return render(request, 'single-post.html', context)

def post_author(request):
    posts = Post.objects.filter(author=request.user).order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request, 'test.html' , context)