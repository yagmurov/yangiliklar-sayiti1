from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(null=True)
    
    def __str__(self):
        return  self.name
    @property
    def count_articles(self):
        count_a=self.articles.all().count()
        return count_a
        
    
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
        



class Article(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=300)
    slug=models.SlugField(null=True, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='articles')
    desc=models.TextField()
    photo=models.ImageField(upload_to='articles/')
    tags=models.CharField(max_length=100, null=True, blank=True)
    views=models.PositiveIntegerField(null=True, default=0)
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Yuklangan vaqti! ")
    updated_at=models.DateTimeField(auto_now=True, verbose_name="Taxrirlangan vaqti! ", null=True, )
    
    
    
    
    def __str__(self):
        return  self.title
    
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
        
    class Meta:
        db_table='articles'
        indexes=[
            models.Index(fields=['title', 'subtitle'])
        ]
        
        