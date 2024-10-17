from django.contrib import admin
from apps.models import Post, Category, UserProfile

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_name', 'date_posted', 'modified_at', 'author')
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(UserProfile)