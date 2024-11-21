from django.contrib import admin
from apps.models import Post, Category, UserProfile, Comment, Tag, WebsiteMeta

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_name', 'date_posted', 'modified_at', 'author')
    prepopulated_fields = {'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Tag, TagAdmin)
admin.site.register(WebsiteMeta)