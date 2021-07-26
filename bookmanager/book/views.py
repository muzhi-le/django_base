from django.shortcuts import render

# Create your views here.
"""
    视图
    所谓的视图，其实就是Python函数
    视图函数有两个要求：
        1.视图函数的第一个参数就是接收请求，这个请求其实就是HttpRequest的类对象
        2.必须返回一个响应
        
"""
from django.http import HttpRequest
from django.http import HttpResponse


# 我们期望用户输入：http://127.0.0.1:8000/index/
# 来访问视图函数
def index(request):

    # return HttpResponse('ok')

    # rander      渲染模板
    # request,      请求
    # template_name,    模板名字
    # context = None

    # 模拟数据查询
    context = {
        'name': '马上双11，点击有惊喜！'
    }

    return render(request, 'book/index.html', context=context)