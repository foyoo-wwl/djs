from django.db import models

# Create your models here.

from datetime import datetime

class City(models.Model):
    name = models.CharField(max_length=20,verbose_name='城市名')
    add_time = models.DateTimeField(datetime.now)
    desc = models.CharField(max_length=200,verbose_name='城市描述')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    click_num = models.IntegerField(default=0,verbose_name='点击数')
    fav_num = models.IntegerField(default=0,verbose_name='收藏数')
    image = models.ImageField(upload_to='org/%y/%m',verbose_name='封面图')
    address = models.CharField(max_length=150,verbose_name='机构地址')
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name='所属结构')
    name = models.CharField(max_length=50,verbose_name='教师名')
    work_years = models.IntegerField(verbose_name="工作年限")
    work_company = models.CharField(max_length=50,verbose_name='公司名称')
    work_position = models.CharField(max_length=50,verbose_name='公司职位')
    points = models.CharField(max_length=50,verbose_name='教育特点')
    click_num = models.IntegerField(default=0,verbose_name='点击数')
    fav_num = models.IntegerField(default=0,verbose_name='收藏数')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
