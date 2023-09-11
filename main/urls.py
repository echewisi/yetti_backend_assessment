from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name= 'home'),
    path('login/', views.custom_login, name='login'),
    path('register/', views.registerview, name='register')
]
