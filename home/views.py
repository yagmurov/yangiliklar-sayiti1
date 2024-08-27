from django.shortcuts import get_object_or_404, render,redirect
from .models import Article, Category
from .forms import TestForm,ArticleForm
# Create your views here.

def article_list(request):
  
    articles=Article.objects.all()
    categories=Category.objects.all()
    context={
        'articles':articles,
        'categories':categories
    }
    return render(request,'index.html', context)


def detail(request, slug):
#     article=Article.objects.filter(slug=slug)
#     if not article:
#         return render(request,'404.html')
    
    
#     context={
#         'article':article.first()
#     }
#     return render(request,'detail.html', context)


    article=get_object_or_404(Article, slug=slug)
    others=Article.objects.filter(category=article.category).exclude(id=article.id)
    
    article.views+=1
    article.save()
    context={
        'article':article,
        'articles':others
        
    }
    return render(request,'detail.html', context)

    

def category_articles(request, slug):
    category=get_object_or_404(Category, slug=slug)
    
    # articles=Article.objects.filter(category=category)
    articles=category.articles.all()
    
    context={
        'category':category,
        'articles':articles
    }
    return render(request,'category_articles.html', context)

def article_creaet(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method=="GET":
        form=ArticleForm()
        context={
            'form':form
        }
        return render(request,'article_create.html', context)

    user=request.user
    data=request.POST
    files=request.FILES
    
    form=ArticleForm(data=data, files=files)
    if form.is_valid():
        print(user)
        form.save()
        return redirect('article_list')
        
        
    
    context={
        'form':form
    }
    return render(request,'article_create.html', context)
    
def update_article(request,slug):
    article=get_object_or_404(Article, slug=slug) 
    if request.method=="GET":
        form=ArticleForm(instance=article)
        context={
            'form':form
        }
        return render(request,'article_update.html', context)

    data=request.POST
    files=request.FILES
    
    form=ArticleForm(data=data, files=files, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article-detail', article.slug)
        
        
    
    context={
        'form':form
    }
    return render(request,'article_update.html', context)

def delete_article(request,id):
    print(id, "@###########################")
    article=get_object_or_404(Article, id=id)
    if request.method=='GET':
        context={
            "article":article
        }
        return render(request,'delete-conf.html', context)
    
    article.delete()
    
    return redirect('article_list')
    

















