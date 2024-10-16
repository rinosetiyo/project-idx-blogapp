from django.utils import timezone
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)  # Category name
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"  # For a better display in the admin

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    content = models.TextField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
