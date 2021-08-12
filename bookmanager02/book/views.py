from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from book.models import BookInfo
def index(request):

    [book.id for book in BookInfo.objects.all()]
    [book.id for book in BookInfo.objects.all()]
    [book.id for book in BookInfo.objects.all()]

    # 缓存
    books = BookInfo.objects.all()
    [book.id for book in books]
    [book.id for book in books]
    [book.id for book in books]

    # 限制查询结果集，用切片处理
    books = BookInfo.objects.all()[0:2]

    # 在这里实现，增删改查
    books = BookInfo.objects.all()
    print(books)

    return HttpResponse('index')


# ==============新增数据===============
# from book.models import BookInfo
# 方式一
book = BookInfo(
    name='Django',
    pub_date='2020-1-1',
    readcount=10
)
# 必须要调用 镀锡的save方法才能将数据保存到数据库中
book.save()

# 方式二
# objects  ----相当于一个代理，实现增删改查
#
BookInfo.objects.create(
    name='测试开发入门',
    pub_date='2020-1-1',
    readcount=100
)

# ============= 修改数据 ===============
# 方式1
# select * from bookinfo where id=6
book = BookInfo.objects.get(id=8)
book.name = '运维开发入门'
book.save()

# 方式2
# filter过滤
BookInfo.objects.filter(id=8).update(name='爬虫入门', commentcount=666)

# ============ 删除数据 ===============
# 方式1
book = BookInfo.objects.get(id=8)

# 删除分2种，物理删除（这条记录的数据删除）和逻辑删除(修改标记位，例如 is_delete=False)
book.delete()

# 方式2
BookInfo.objects.filter(id=5).delete()

# ============== 查询 ==================
# get查询单易结果，如果不存在会抛出模型类，DoesNotExist异常
try:
    book = BookInfo.objects.get(id=1)
except:
    print("查询结果不存在")

# all查询多个结果
BookInfo.objects.all()
from book.models import PeopleInfo
PeopleInfo.objects.all()

# count查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()

# =========== 过滤查询 ==============
# 实现SQL种的where功能，包括
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果
# 模型类名.objects.filter(属性名__运算符=值)       获取n个结果 n=1,2,3,.....
# 模型类名.objects.exclude(属性名__运算符=值)      获取n个结果 n=1,2,3,.....
# 模型类名.objects.get(属性名__运算符=值)          获取1个结果 或者 异常

# 查询编号为1的图书
BookInfo.objects.get(id=1)       # 简写形式  (属性名=值)
BookInfo.objects.get(id__exact=1)   # 完整形式  (id__exact=1)
BookInfo.objects.get(pk=1)  # pk primary key 主键

BookInfo.objects.get(id=1)        # 得到的是一个
BookInfo.objects.filter(id=1)     # 得到的是列表

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains="湖")
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith="部")
# 查询书名为空的图书
# select * from bookinfo where name is null;
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
# select * from bookinfo where id in (1,3,5);
BookInfo.objects.filter(id__in=[1, 3, 5])

# 查询编号大于3的图书
# 大于    gt      great  大的
# 大于等于 gte     equal  相等
# 小于    lt
# 小于等于 lte
BookInfo.objects.filter(id__gt=3)

# 查询编号不等于3的书籍
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt="1990-1-1")

# =========== F对象 ===========
from django.db.models import F
# 使用：2个属性的比较
# 语法形式：以filter为例    模型类名.objiects.filter(属性名__运算符=F("第二个属性名"))

# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F("commentcount"))

# 查询阅读量大于等于评论量2倍的图书
BookInfo.objects.filter(readcount__gte=F("commentcount")*2)

# ======== Q对象 ============
# &：与， |：或， ~：非
# 并且查询
# 查询阅读量大于20，并且编号小于3的图书
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# 或者
BookInfo.objects.filter(readcount__gt=20, id__lt=3)

# 或者查询
# 或者语法格式： 模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值))
# 并且语法格式： 模型类名.objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值))
# 查询阅读量大于20，或者编号小于3的图书

from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))

# 查询编号不等于3的书籍
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))

# =========== 聚合函数 =========

from django.db.models import Sum,Max,Min,Avg,Count

# 模型类名.objects.aggregate(Xxx("字段名"))
# 统计所有书籍的阅读量总共有多少个
BookInfo.objects.aggregate(Sum("readcount"))

# ============== 排序 ================
# 根据阅读量排序
# select * from bookinfo order by readcount;    #  SQL语句写法，阅读量从小到大
# select * from bookinfo order by readcount desc;   #  SQL语句写法，阅读量从大到小
BookInfo.objects.all().order_by("readcount")  # 阅读量从小到大排序
BookInfo.objects.all().order_by("-readcount")   # 阅读量从大到小排序

# ============= 级联查询 ==========

# 查询书籍为1的所有人物信息
# 获取了id为1的书籍
book = BookInfo.objects.get(id=1)  # 先找到书籍
book.peopleinfo_set.all()          # 通过书籍找人物，形成关联查询，BookInfo.objects.filter(book=1)也能实现相同效果

# 查询人物为1的书籍信息
person = PeopleInfo.objects.get(id=1)
person.book.name    # 人物信息
person.book.readcount   # 阅读量信息

# ========= 关联过滤查询 ==========

# 语法格式：
# 查询1的书籍，条件为n
# 模型类名.objects.filter(关联模型类名小写__字段名__运算符=值)

# 查询图书，要求图书人物为“郭靖”
BookInfo.objects.filter(peopleinfo__name__exact="郭靖")
BookInfo.objects.filter(peopleinfo__name="郭靖")

# 查询图书，要求图书中人物的描述包含“八”
BookInfo.objects.filter(peopleinfo__description__contains="八")

# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name="天龙八部")
PeopleInfo.objects.filter(book__name__exact="天龙八部")

# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)