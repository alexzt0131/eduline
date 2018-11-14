from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name='昵称')
    # 生日,可为空
    birthday = models.DateTimeField(verbose_name='生日', null=True, blank=True)
    # 性别,默认为女
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
    # 地址
    address = models.CharField(max_length=100, verbose_name='地址')
    # 手机号，可为空
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机')
    # 图片，默认图片为deault.png(需要自己在对应文件夹中存储)，upload_to为上传路径，记住图片字段必须有字段最大值
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100, verbose_name='图片')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    '''
    邮箱验证码
    '''
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name="验证码类型",
                                 choices=(('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')),
                                 max_length=30)
    # 这里的now得去掉(),如果不去掉则会根据编译时间，而不是我们要的实例化时间。
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


class Banner(models.Model):
    '''
    轮播图
    '''
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(max_length=100, upload_to='banneer/%Y/&m', verbose_name="轮播图")
    url = models.URLField(max_length=200, verbose_name='访问地址')
    # index的值默认越大越靠后，可以自定义修改index值。
    index = models.IntegerField(default=100, verbose_name='轮播顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
