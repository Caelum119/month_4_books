from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_post, name='book_post'),
]
