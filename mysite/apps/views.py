from django.shortcuts import render, get_object_or_404
from apps.models import Post, Comment, Category, WebsiteMeta
from apps.forms import CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-date_posted')
    featured_blog = Post.objects.filter(is_featured=True).order_by('-date_posted')

    if featured_blog:
        featured_blog = featured_blog[0]
    else:
        featured_blog = None

    if WebsiteMeta.objects.all().exists():
        meta = WebsiteMeta.objects.all()[0]
    else:
        meta = None

    context = {
        'posts': posts
    }
    return render(request,'index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories =  Category.objects.all()
    comment_form = CommentForm()
    comments = Comment.objects.filter(post=post, parent=None)
    comment_count = comments.count()
    post.view_count += 1
    post.save()

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            if request.POST.get('parent'):
                # save reply
                parent = request.POST.get('parent')
                parent_obj = Comment.objects.get(id=parent)
                if parent_obj:
                    comment_reply = comment_form.save(commit=False)
                    comment_reply.parent = parent_obj
                    comment_reply.post = post
                    comment_reply.save()
            else:      
                comment = comment_form.save(commit=False)
                postid = request.POST.get("post_id")
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