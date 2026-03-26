from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class UserInfo(models.Model):
  name = models.CharField(max_length=20, verbose_name='用户名')
  password = models.CharField(max_length=20, verbose_name='密码')
  age = models.IntegerField(verbose_name='年龄', null=True, blank=True, default=2) # 数据迁移时，对于已有的数据，新增该字段时：默认为2
  size = models.FloatField(verbose_name='身高', null=True, blank=True, default=None) # 数据迁移时，对于已有的数据，新增该字段时：默认为null, 空值


class Student(models.Model):
  # 自增主键, django会默认创建
  # id = models.AutoField(primary_key=True)        # int    类型
  # id = models.BigIntegerField(primary_key=True)  # bigint 类型

  name = models.CharField(max_length=20, verbose_name='姓名')
  age = models.IntegerField(
    verbose_name='年龄', 
    blank=True,  # 可选：允许空值
    null=True,   # 可选：数据库层面允许 NULL
    # 可选：限制值(django 层面约束, 不限制数据库表中该字段的值)
    validators=[
      MaxValueValidator(100, message='年龄不能大于100岁'),
      MinValueValidator(0, message='年龄不能小于0岁'),
    ]
  )

  # django 层面上的约束
  choices = (
    (1, '男'),
    (2, '女'),
  )
  sex = models.SmallIntegerField(verbose_name='性别', choices=choices)

  # 数据库层面的约束
  # on_delete = models.CASCADE 级联删除(班级删除, 学生也删除); 
  # on_delete = models.SET_NULL 删除数据时, 设置为NULL(班级删除, 学生也删除); 
  # --- ！！！注： 该字段有允许为空, 需添加blak=True, null=True
  grade = models.ForeignKey(to='Grade', to_field='id', verbose_name='班级ID', on_delete=models.CASCADE)



class Grade(models.Model):
  name = models.CharField(max_length=10, verbose_name='班级名称')