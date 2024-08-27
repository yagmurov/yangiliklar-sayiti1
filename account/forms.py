from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password=forms.CharField()
    confirm_password=forms.CharField()
    
    class Meta:
        model=User
        fields=['username', 'email','first_name','last_name']
    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if not password or not confirm_password:
            raise forms.ValidationError(" password yozilmadi! ")
        if password!=confirm_password:
            raise forms.ValidationError(" parollar bir xil emas! ")
            
        return password
    
    def save(self, commit=True):
        user=super().save(commit)
        password=self.cleaned_data.get('password')
        user.username=self.cleaned_data.get('email')
        user.set_password(password)
        return user
    
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        if not username or not password:
            raise forms.ValidationError(" Username va passwordni to'g'ri kiriting! ")
        
        return self.cleaned_data
        

class PasswordResetForm1(forms.Form):
    username=forms.CharField()
    def clean(self):
        username=self.cleaned_data.get('username')
        if not username :
            raise forms.ValidationError(" Username  to'g'ri kiriting! ")
        
        user=User.objects.filter(username=username)
        if not user.exists():
            raise forms.ValidationError(" Username topilmadi! ")
        return self.cleaned_data
    
class UpdatePassword(forms.Form):
    old_password=forms.CharField()
    new_password=forms.CharField()
    confirm_password=forms.CharField()
    
   
    
    def clean_confirm_password(self):
        new_password=self.cleaned_data.get('new_password')
        confirm_password=self.cleaned_data.get('confirm_password')

        
        if  not new_password or not confirm_password:
            raise  forms.ValidationError(" Parolni to'liq kiriting: ")
        
        if new_password!=confirm_password:
            raise forms.ValidationError(' Parol bir xil emas!')     
        
        return new_password   

    