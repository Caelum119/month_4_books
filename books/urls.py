from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='book_posts'),      
    path('<int:id>/', views.book_detail_view, name='book_detail'), 
    path('about/', views.book_post, name='book_post'),        
]
