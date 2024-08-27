from django.urls import path
from .views import registration,login_user,logout_user,password_reset,update_password
urlpatterns = [
    path("signup/", registration, name='signup'),
    path("login/", login_user, name='login'),
    path("logout_user/",logout_user, name='logout_user' ),
    path("password_reset/",password_reset, name='password_reset' ),
    path("update_password/",update_password, name='update_password' ),
    
    
    
]
