from django.db import models

# Create your models here.
'''
    1.我们的模型类，需要继承自models.Model
    2.系统会自动为我们添加一个主键--id字段
    3.字段的定义：
        字段名=model.类型（选项）  //字段名其实就是数据表的字段名，字段名不要使用Python，MySql等关键字
'''


# 书籍
class BookInfo(models.Model):
    name = models.CharField(max_length=10)


# 人物
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()  #
    # 外键约束：人物属于那本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

