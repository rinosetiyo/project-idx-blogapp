from django.utils import timezone
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.CharField(max_length=200)
    bio = models.TextField(blank=True)  # Optional bio
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)  # Optional profile picture

    def __str__(self):
        return self.user
        
class Category(models.Model):
    name = models.CharField(max_length=100)  # Category name
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"  # For a better display in the admin

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    content = models.TextField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title
