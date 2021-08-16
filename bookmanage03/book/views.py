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
    # http://127.0.0.1:8000/a/11/?order=readcount&page=1&order=commentcount
    query_params = request.GET   # < QueryDict: {'order': ['readcount']} >
    # print(query_params)
    # order = query_params.get('order')   # readcount
    # order = query_params['order']   # readcount
    # print(order)
    # QueryDict 具有字典的特性，还具有一件多值
    order = query_params.getlist("order")
    print(order)

    return HttpResponse('aaa')
