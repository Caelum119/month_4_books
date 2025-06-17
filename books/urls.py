from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='book_posts'),         # /news_posts/
    path('<int:id>/', views.book_detail_view, name='book_detail'),  # /news_posts/1/
    path('about/', views.book_post, name='book_post'),         # optional: /news_posts/about/
]
