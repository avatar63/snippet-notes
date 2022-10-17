from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('newpost/',views.newpost,name='newpost'),
    path('newpost/newpostadd/',views.newpostadd,name='newpostadd'),
    path('register/newuser/',views.newuser,name='newuser'),
    path('profile/',views.profile,name='profile'),
    path('logdata/',views.logdata,name='logdata'),
    path('home/delete/<int:id>',views.delete, name='delete'),
    path('home/edit/<int:id>',views.edit, name='edit'),
    path('home/edit/editpost/<int:id>',views.editpost, name='editpost'),
    
]