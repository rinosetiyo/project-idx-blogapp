from django.shortcuts import render, get_object_or_404
from apps.models import Post, Comment, Category
from apps.forms import CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request,'index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories =  Category.objects.all()
    comment_form = CommentForm()
    comments = Comment.objects.filter(post=post)
    comment_count = comments.count()
    post.view_count += 1
    post.save()

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            postid = request.POST.get("post_id")
            authorid = request.POST.get("author_id")
            post = Post.objects.get(id=postid)
            comment.post = post
            comment.save()

    context = {
        'post': post,
        'categories': categories,
        'comment_form': comment_form,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'single-post.html', context)

def post_author(request):
    posts = Post.objects.filter(author=request.user).order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request, 'test.html' , context)