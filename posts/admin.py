from django.contrib import admin

from .models import Post

# Register your models here.



class Product_Admin(admin.ModelAdmin):
    list_display=['title','content','draft']
    list_filter=['draft']
    search_fields=['title']



admin.site.register(Post,Product_Admin)
