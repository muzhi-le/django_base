from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo

# Create your views here.

def create_book(request):

    book = BookInfo.objects.create(
        name='abc',
        pub_date='2000-1-1',
        readcount=10
    )

    return HttpResponse("create")

def shop(request, city_id, shop_id):

    return HttpResponse('aaa')