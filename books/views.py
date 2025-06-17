from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.shortcuts import get_object_or_404



def book_list_view(request):
  if request.method == 'GET':
    book_list = models.Book.objects.all().order_by('-id')
    context = {
      'book_list': book_list,
    }
    return render(request, template_name='book.html', context=context)

def book_detail_view(request, id):
  if request.method == 'GET':
    book_id = get_object_or_404(models.Book, id=id)

    context = {
      'book_id': book_id,
    }
    return render(request, template_name='book_detail.html', context=context)














def book_post(request):
    if request.method == 'GET':
        return HttpResponse("📚 I love reading books about fantasy and adventure!")
