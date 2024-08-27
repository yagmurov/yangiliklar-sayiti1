from django.urls import path
from .views import article_list,detail,category_articles, article_creaet,update_article,delete_article

urlpatterns = [
    path('', article_list,name='article_list'),
    path('detail/<str:slug>', detail,name='article-detail'),
    path('category/<str:slug>', category_articles,name='category-articles'),
    path('create/', article_creaet, name='create'),
    path('update/<str:slug>', update_article,name='update'),
    path('delete/<int:id>', delete_article ,name='delete'),
    
    
    
]
