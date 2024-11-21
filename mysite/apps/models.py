from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)  # User model
    bio = models.TextField(blank=True)  # Optional bio
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)  # Optional profile picture

    def __str__(self):
        return self.user.first_name
        
class Category(models.Model):
    name = models.CharField(max_length=100)  # Category name
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"  # For a better display in the admin

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    content = models.TextField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    is_featured = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date_posted = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='replies')

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-date_posted']

class WebsiteMeta(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    about = models.TextField()
    
    def __str__(self):
        return self.title

