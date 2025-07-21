from django.db import models
# User类是Django内置的用户认证模型，提供了用户管理功能
# 包含用户名、密码、邮箱等基本字段，用于系统登录认证
# 在此导入是为了与其他模型（如Student）建立关联关系
from django.contrib.auth.models import User
from grades.models import Grade

# Create your models here.
GENDER_CHOICES = [
    ('M','男'),
    ('F','女'),
]

class Student(models.Model):
    student_number = models.CharField(max_length=20,unique=True,verbose_name='学号')
    student_name = models.CharField(max_length=20,verbose_name='姓名')
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,verbose_name='性别')
    berthday = models.DateField(verbose_name='出生日期',help_text='格式例如：2025-05-01')
    contact_number = models.CharField(max_length=20,verbose_name='联系方式')
    address = models.TextField(verbose_name='家庭住址')

    # user表一对一关联
    # 这里创建了与Django内置User模型的一对一关系
    # OneToOneField表示每个学生记录对应唯一一个用户账号
    # on_delete=models.CASCADE意味着当关联的用户被删除时，学生记录也会被删除
    # null=True允许数据库中该字段可以为空
    # blank=True允许表单提交时该字段可以为空
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    # 班级表一对多关联
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE,verbose_name='班级')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = '学生信息'
