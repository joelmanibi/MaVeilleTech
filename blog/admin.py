from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle1', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'subtitle']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)

# Register your models here.
