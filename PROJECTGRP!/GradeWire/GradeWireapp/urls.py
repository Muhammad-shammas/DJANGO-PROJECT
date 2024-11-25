from django.urls import path
from  . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('tlogin/', views.teacherLogin,name='teacherLogin'),
    path('tregister/', views.teacherRegister,name='teacherRegister'),

]
