from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.shortcuts import get_object_or_404
from .models import Book, Review
from django.db.models import Avg
from django.core.paginator import Paginator





def book_list_view(request):
  if request.method == 'GET':
    book_list = models.Book.objects.all().order_by('-id')
    context = {
      'book_list': book_list,
    }
    return render(request, template_name='book.html', context=context)

def book_detail_view(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(choice_book=book)
    avg_rating = book.average_rating()

    

    context = {
        'book': book,
        'reviews': reviews,
        'avg_rating': avg_rating,
    }
    return render(request, 'book_detail.html', context)


def book_post(request):
    if request.method == 'GET':
        return HttpResponse("📚 I love reading books about fantasy and adventure!")
