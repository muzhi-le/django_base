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

    """
    查询字符串
        http://127.0.0.1:8000/a/11/?order=readcount&page=1&order=commentcount
        url 以 ? 号为分隔， 分为两部分
        ?号前边为请求路径
        ?号后边为查询字符串，查询字符串类似于字典，key=value，多个数据采用&拼接
    """

    query_params = request.GET   # < QueryDict: {'order': ['readcount']} >
    # print(query_params)
    # order = query_params.get('order')   # readcount
    # order = query_params['order']   # readcount
    # print(order)
    # QueryDict 具有字典的特性，还具有一件多值
    order = query_params.getlist("order")
    print(order)

    return HttpResponse('aaa')

def register(request):

    data = request.POST    # 接受用户传递过来的请求
    print(data)
    return HttpResponse("ok")
