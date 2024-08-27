from django import forms
from .models import Article

#Form
#ModelForm

class TestForm(forms.Form):
    first_name=forms.CharField( max_length=50)
    last_name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    
    
    def clean_first_name(self):
        first_name=self.cleaned_data('first_name')
        
        return first_name
    
    
class ArticleForm(forms.ModelForm):
    user=forms.CharField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = Article
        fields = ('user','title', 'subtitle','desc', 'category','photo','tags')
        
        
    def clean_title(self):
        title=self.cleaned_data.get('title')  
        if len(title)<10:
            raise forms.ValidationError(" Title juda kam. Kamida 10 ta belgi bo'lsin ")
        return title
    
    def clean(self):
        subtitle=self.cleaned_data.get('subtitle')  
        if len(subtitle)<15:
            raise forms.ValidationError(" Title juda kam. Kamida 15 ta belgi bo'lsin ")
        return self.cleaned_data
        
    def save(self,commit=True,*args, **kwargs):
        article=super().save( commit=commit,*args, **kwargs)
        return article
            
        