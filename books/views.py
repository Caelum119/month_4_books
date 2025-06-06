from django.shortcuts import render
from django.http import HttpResponse

def book_post(request):
    if request.method == 'GET':
        return HttpResponse("📚 I love reading books about fantasy and adventure!")
