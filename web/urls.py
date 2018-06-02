# -*- coding: utf8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContentListView.as_view()),
    path('content/<int:pk>', views.ContentDetailView.as_view()),
    path('content/create/', views.ContentCreate.as_view()),  
    path('content/<int:pk>/update/', views.ContentUpdate.as_view()),
    path('user/', views.UserListView.as_view()),  
    path('user/create/', views.UserCreate.as_view()),  
    path('user/<int:pk>/update/', views.UserUpdate.as_view()),  
    path('user/<int:pk>/password/update/', views.PasswordUpdate.as_view()),    
]