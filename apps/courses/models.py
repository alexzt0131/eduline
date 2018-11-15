from django.db import models
from datetime import datetime


# Create your models here.

# 课程信息
class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="课程名")
    # 描述这一块，我们先用TextField，因为它允许我们不输入长度,而且可以输入值无范围，之后再更新为富文本形式
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(max_length=500, verbose_name="课程详情")
    is_banner = models.BooleanField(default=False, verbose_name="是否轮播")
    degree = models.CharField(max_length=2,
                              choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), verbose_name="难度等级")
    # 学习数这里使用分钟数作计量单位，便于后台记录(存储最小单位)和前台转换
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟数）")
    # 学习人数从点击开始学习算起
    students = models.IntegerField(default=0, verbose_name="学习人数")
    # 收藏人数从点击收藏按钮算起
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to='courses/%Y/%m', max_length=100, verbose_name="封面图片")
    # 点击数从点击页面算起
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    category = models.CharField(default="后端开发", max_length=20, verbose_name="课程类别")
    tag = models.CharField(default='', max_length=10, verbose_name="课程标签")
    youneeded_know = models.CharField(default='', max_length=300, verbose_name="课程须知")
    teacher_tell = models.CharField(default='', max_length=300, verbose_name="老师告诉你")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



# 章节信息
class Lesson(models.Model):
    # 前面知道一个课程对应多个章节，所以在章节表中将课程设置为外键。
    # 此处的course其实就是一个用来告诉我们这个章节属于哪个课程的字段
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        # 采用了字符串的格式化方式来同时引用多个数据
        return '<<{0}>>课程的章节》{1}'.format(self.course, self.name)



# 视频信息
class Video(models.Model):
    # 前面知道一个章节对应多个视频，所以在视频表中将章节设置为外键。
    # 此处的lesson其实就是一个用来告诉我们这个视频属于哪个章节的字段
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="章节")
    name = models.CharField(max_length=100, verbose_name="视频名称")
    url = models.URLField(max_length=200, default='', verbose_name="访问地址")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟数）")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<<{0}>>章节的视频》{1}'.format(self.lesson, self.name)  # return self.name也是可以



# 课程资料信息
class CourseResource(models.Model):
    # 前面知道一个课程对应多个课程资料，所以在课程资料表中将课程设置为外键。
    # 此处的course其实就是一个用来告诉我们这个课程资料属于哪个课程的字段
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="名称")
    download = models.FileField(max_length=100, upload_to='course/resource/%Y/%m',
                                verbose_name="资源文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<<{0}>>课程的课程资料》{1}'.format(self.course, self.name)  # return self.name也行