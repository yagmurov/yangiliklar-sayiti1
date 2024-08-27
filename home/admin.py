from django.contrib import admin
from .models import Article,Category
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['id','title','views','created_at','updated_at']
    prepopulated_fields={'slug':['title']}
    readonly_fields=( "created_at",'updated_at')
    
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']
    prepopulated_fields={'slug':['name']}
    