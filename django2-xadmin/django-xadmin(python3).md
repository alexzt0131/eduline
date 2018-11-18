# python3.6+django2.0-xadmin-imooc学习记录 #

# 开发基础环境搭建 #

	python与模块版本：
		python==3.6.4
		django==2.0.1
		pip 最新
## 1安装python3.6 ##
	下载地址：https://www.python.org/downloads/release/python-364/
	直接安装即可
## 2设置环境变量 ##
	python3 安装文件点击设置环境变量即可
	python2 在PATH中最后添加新安装python的路径如（c:\python27;C:\Python27\Scripts;）Scriptsm目录是模块执行的目录如virtualenv 模块pip、mkvirtualenv等，分号别忘记。
## 3先安装setuptools ##
	python3安装包集成
	下载地址：https://pypi.python.org/pypi/setuptools#downloads
	将下载后的tar文件解压，用CMD模式进入到解压后的文件所在的目录执行命令：python setup.py install
## 4安装pip ##
	python3安装包集成
	下载地址：https://pypi.python.org/pypi/pip#downloads
	将下载后的tar文件解压，用CMD模式进入到解压后的文件所在的目录执行命令:python setup.py install 
## 5安装virtualenv ##
	执行命令 pip install virtualenv
	如果找不到文件或者网络慢可使用国内的pip源地址
		
	阿里云 http://mirrors.aliyun.com/pypi/simple/
	
	中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
	
	豆瓣(douban) http://pypi.douban.com/simple/
	
	清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
	
	中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

	使用命令：pip install web.py -i http://pypi.douban.com/simple

	如果报错使用：pip install web.py -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

	如果想配置成默认的源，方法如下：
	
		需要创建或修改配置文件（一般都是创建），
		
		linux的文件在~/.pip/pip.conf，
		
		windows在%HOMEPATH%\pip\pip.ini），
		
		修改内容为：
		
		[global]
		index-url = http://pypi.douban.com/simple
		[install]
		trusted-host=pypi.douban.com
	
	
	新建虚拟环境：virtualenv d:\test4 提示结束后转到 test4目录下Script目录运行active激活当前虚拟环境，控制台符号变为(test4) d:\test4\Scripts>，如需退出执行deactive命令即可。
## 6安装virtualenvwrapper ##
	由于virtualenv每次都要进入虚拟环境目录这样很麻烦所以需要安装virtualenvwrapper模块
	
	安装及使用方法：

	0.首先需要在系统变量中指定一个默认的WORKON_HOME的变量，即所有创建的虚拟环境的存放目录，如：d:\virtualnevs 注意不加冒号。（如果不能正常运行，就讲python安装目录中Script目录中的所有文件copy到指定的workon目录中）。
	
	1.安装虚拟环境

	pip install virtualenvwrapper-win ，linux可以去掉-win
	
	2.创建虚拟环境
	会在你当前用户下创建一个Env的文件夹，然后将这个虚拟环境安装到这个目录下
	
	mkvirtualenv 环境名称
	
	3.进入某个虚拟环境
	
	workon 环境名称
	
	4.退出当前环境
	
	deactivate
	
	5.列出全部虚拟环境
	
	lsvirtualenv
	
	6.删除某个虚拟环境
	
	rmvirtualenv 环境名称
	
	7.进入到虚拟环境所在的目录
	
	cdvirtualenv

	不知道你注意没有，这个dajngoTest是灰色的，
	我们可以右键mark为source Root目录，就变成了蓝色，
	这样做的好处就是可以避免包的导入问题，我们在import模块时pycharm会根据设置从而智能提示。如果不mark可能会出现很多我们在pycharm中报红色，但是cmd可以运行的情况。

# Django基础知识 #
## Django的目录结构 ##
	需要新建几个目录：
		0.与工程名相同	存放工程文件的文件夹
		1.apps	  		存放web应用的文件夹
		2.log 	  		存放日志文件的文件夹
		3.static  		存放js、css及图片的文件夹
		4.media			存放用户上传文件的文件夹
		5.template		存放静态页面的文件夹

	在pycharm中可以将apps markdirectory as sourceroot，这样就可以在引入app中文件时不用添加apps了，不过在命令行中就会报错，解决方法是在settings.py中将apps文件夹插入进来加入一下代码即可：
	sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
	
## Django与mysql的链接 ##

	settings.py中设置：
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': '你的库名',
	        'USER': '账号',
	        'PASSWORD': '密码',
	        'HOST': '127.0.0.1',#本机可不改
	    }
	}
	数据库需要自己创建，django只会生成表。
	建好数据库使用manager命令 makemigrations -> migration来生成数据表
	报错的话需要安装mysqlclient，最好下载到本地安装，地址：https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
	页面上面的cp36代表Python3.6的版本，cp37代表Python3.7 的版本！
	然后在虚拟环境安装：pip install mysqlclient-1.3.13-cp36-cp36m-win_amd64.whl（随着更新可能会不一样版本）
	
	**运行django工程时可能会发生的错误**
	#链接mysql数据库时报错，django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named MySQLdb
	#如果pip安装后还是提示这个错误，一定要先注意看安装MySQLdb用的是否是venv的python pip 不要用环境变量中的pip那样不会装到venv中，这个问题坑了我半个多小时。
	#win7下有可能会需要这两个dll拷贝到system32中：libguide40.dll、libmmd.dll
	#提供一个驱动下载的地址以防网络不好或者提示没有对应版本，注意python27 32位选win32的64选amd64的
	#https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
	
	

## 静态文件的处理 ##
	
	在settings中debug为true的情况下：
		例如引用static文件夹中的style.css文件页面上直接写入/static/css/style.css是无效的，需要在settings文件中增加一个列表
		STATICFILES_DIRS = [
		    os.path.join(BASE_DIR, 'static')
		]
		重启django这样就可以访问静态文件了。
	在settings.py中如果写了中文注释，python3没问题，python27需要再第一行加上#coding:utf-8	


# 留言板app #
## 创建app liuyan拷贝到apps文件夹中并生成数据库表makemigrations， migrate。 ##
## 拷贝start.html文件，设置路由 ##
	
## 使用*对象关系映射*ORM来穿件UserMessage表的model ##
	'
	class UserMessage(models.Model):   # 继承于django.db.models.Model
		# max_length设置最大长度，verbose_name在后台显示字段会用到，也就是中文显示文本内容
	    name = models.CharField(max_length=20, verbose_name="昵称")  
	    email = models.EmailField(verbose_name="邮箱")
	    address = models.CharField(max_length=100 ,verbose_name="联系地址")
	    message = models.CharField(max_length=500, verbose_name="你的轨迹")
	
	    class Meta:
	        verbose_name = "用户留言信息"
		# class Meta，内嵌于 UserMessage 这个类的定义中，主要是用于后台管理显示中文信息
	'


	表的id是自动生成的，如果需要自定义主键,那么需要在models.py中添加字段：

	'object_id = models.CharField(primary_key=True,max_length=100 ,verbose_name="主键")'


	**Meta的说明**

		1、在Meta信息中我们可以指定表的名称，如db_table：
		
		'db_table = "user_liuyan"'
		
		2、可以指定排序的字段，如ordering：
		
		'ordering = 'object_id''
		
		这是以其升序的，倒序的话只需要这样ordering = '-object_id'即可。
		
		3、可以更改后台信息，如verbose_name_plural：
		
		verbose_name_plural是verbose_name的复数形式，如果不改则会在其后面加s。
		
		'verbose_name = "用户留言信息"'
		则verbose_name_plural 会显示 "用户留言信息s"，所以一般这2个的值都是相同的
		即
		'verbose_name =verbose_name_plural="用户留言信息"'
## models的增删改查 ##
** 不多做介绍 **
## html页面提交数据并存入数据库 ##
	*注意html form表单中添加 {% csrf_token%}
	*并且views.py中可以定义class来代替函数，然后在路由中使用views.class.as_view()方法指定路由指向
	
	
## 送官方关于Built-in template tags and filters的介绍 ##
	[https://docs.djangoproject.com/en/2.0/ref/templates/builtins/](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/)

## Django模板语言 ##
	变量

	变量看起来就像是这样： {{ variable }}。
	
	点号(.)用来访问变量的属性。从技术上来说，当模版系统遇到点(“.”)，它将以这样的顺序查询：
	
	    字典查询（Dictionary lookup）
	    属性或方法查询（Attribute or method lookup）
	
	数字索引查询（Numeric index lookup）
	过滤器
	
	过滤器看起来是这样的：{{ name|lower }}。这将在变量 {{ name }} 被过滤器 lower 过滤后再显示它的值，该过滤器将文本转换成小写。使用管道符号 (|)来应用过滤器。 
	
	过滤器参数包含空格的话，必须被引号包起来；例如，使用逗号和空格去连接一个列表中的元素，你需要使用 {{ list|join:”, ” }}。
	
	    常用的模版过滤器：
	    default，如果一个变量是false或者为空，使用给定的默认值。否则，使用变量的值。例如：{{ value|default:"nothing" }}undefined
	    length，返回值的长度。它对字符串和列表都起作用。例如：{{ value|length }}undefined
	    filesizeformat，将该数值格式化为一个 “人类可读的” 文件容量大小 （例如 ‘13 KB’, ‘4.1 MB’, ‘102 bytes’, 等等）。例如：{{ value|filesizeformat }}标签
	
	标签看起来像是这样的： {% tag %}。标签比变量复杂得多：有些用于在输出中创建文本，有些用于控制循环或逻辑，有些用于加载外部信息到模板中供以后的变量使用。 
	
	有些标签需要开始标签和结束标签（例如{% tag %} … tag contents … {% endtag %}）。 
	
	常用的标签：
	
	    for
	    if，elif，else
	
	block和extend
	注释
	
	要注释模版中一行的部分内容，使用注释语法 {# #}. 
	
	例如，这个模版将被渲染为 ‘hello’：{# greeting #}hello
	
	如果想了解更多信息，可以参考这篇文章：[Django-模板（模板语言）](https://blog.csdn.net/qq_14898613/article/details/61196500 "Django-模板（模板语言）")

## URL的别名设置小贴士 ##
	
	在我们这个留言项目中，如果我们在djangoTest/urls.py里面为'start/'添加别名：
	
	原来的路径：
	path('start/', getstart)
	现在的路径：
	path('start/', getstart, name = "get_start")
	
	然后在start.html中修改action地址为下面所示：
	
	<form action="{% url "get_start" %}" method="post" class="smart-green">
	
	这样做的好处就是，如果我们改动urls.py中的'start'不需要再去修改前端代码中url的指向地址。



# 教育网站开发 #

## 配置环境 ##
		需求 开发基础环境搭建 章节内的环境已经搭建完毕
		创建虚拟环境
			'mkvirtualenv eduline'
		安装Django2.0.1
			'pip install django==2.0.1 -i https://pypi.tuna.tsinghua.edu.cn/simple'
		创建Django项目eduline
		
		安装mysqlclient
		配置settings.py中的数据库
		'
		DATABASES = {
		    'default': {
		        'ENGINE': 'django.db.backends.mysql',
		        'NAME': 'eduline',
		        'USER': 'root',
		        'PASSWORD': 'password',
		        'HOST': "127.0.0.1"
		    }
		}
		'
		手动创建eduline数据库，设置charset=utf8
## 安装Xadmin、DjangoUeditor##
	扩展-- 还有一个叫做django-suit的插件，它其实只是美化了admin，功能上并没有做过多的拓展，这里开启传送大门，有兴趣的可以了解一下：http://djangosuit.com/
	[https://github.com/liyaopinner/mxonline_resources](https://github.com/liyaopinner/mxonline_resources "下载地址")
	
		
## 业务逻辑 ##

	'点击个人中心: 你可以修改头像，密码，邮箱，可以看到我的课程以及我的收藏。还可以删除我的收藏，消息。
	
	点击导航栏: 你可以看到公开课，授课讲师，授课机构和全局搜索。
		
	点击公开课：你可以看到课程列表，排序-搜索。热门课程推荐和课程的分页。
	
	点击课程：你可以在课程详情页中对课程进行收藏和取消收藏。同时可以采用富文本对课程内容进行展示。
	
	点击开始学习：你可以看到课程的章节信息和评论信息以及课程资源的下载链接。
	
	点击授课讲师：你可以看到授课讲师的列表页，可以对讲师进行人气排序以及分页，右侧还有讲师排行榜。
	
	点击讲师的详情页面：你可以对讲师进行收藏和分享，以及看到该讲师的全部课程。
	
	点击导航栏: 你可以看到授课机构，它有分页，排序和筛选功能。
	
	机构列表页右侧有快速提交我要学习的表单，之后你便可以开始学习了。
	
	点击机构：它的左侧会呈现：机构首页,机构课程，机构介绍，机构讲师这四部分。
	
	后台管理系统可以切换主题。左侧每一个功能都有列表显示,具有增删改查，筛选功能。
	
	课程列表页可以对不同字段进行排序。你可以选择多条记录进行删除操作。
	
	课程列表页：点击过滤器，选择字段范围开始搜索,结果可以导出csv，xml，json等格式文本。
	
	你可以在课程新增页面上传图片，和进行富文本的编辑，时间选择，添加章节，添加课程资源等。
	
	日志记录：它可以记录后台人员的操作情况。
	
	其他的大家可以在后期的学习过程中慢慢体会，这里就不一一而足了。'

	
	app一共有4个，用于分别实现不同的功能，具体如下：

		**(users)用户版块：**负责记录用户的个人信息，轮播图等相关内容
		**(course)课程版块：**用于记录课程相关的内容
		**(organization)授课教师与授课机构板块：**用于记录授课讲师，机构相关内容
		**(operation)用户操作板块：**用于记录用户操作的相关内容。

## 将代码传到github ##
	我还是使用gitcmd来执行比较顺手


## 数据库字段的定义1 ##
	*users app
		startapp users
		使用继承AbstractUser类来扩展user
		user表的自定义方法官方文档已经给出了，这里开启传送大门https://docs.djangoproject.com/zh-hans/2.0/ref/models/fields/
		
		'from django.contrib.auth.models import AbstractUser
		from django.db import models
		
		# Create your models here.
		
		class UserProfile(AbstractUser):
		    #昵称
		    nick_name = models.CharField(max_length=50, verbose_name='昵称')
		    #生日,可为空
		    birthday = models.DateTimeField(verbose_name='生日', null=True, blank=True)
		    #性别,默认为女
		    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
		    #地址
		    address = models.CharField(max_length=100, verbose_name='地址')
		    #手机号，可为空
		    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机')
		    #图片，默认图片为deault.png(需要自己在对应文件夹中存储)，upload_to为上传路径，记住图片字段必须有字段最大值
		    image = models.ImageField(upload_to='image/%Y/%m', default = 'image/default.png', max_length=100, verbose_name='图片')
		
		    class Meta:
		        verbose_name = '用户信息'
		        verbose_name_plural = verbose_name
		
		    def __str__(self):
		        return self.username'
		注册APP和重载AUTH_USER_MODEL
			在settings.py中配置		
			INSTALLED_APPS中添加app_name
			AUTH_USER_MODEL重新赋值为
				AUTH_USER_MODEL = 'users.UserProfile'
		生成数据库表
			makemigrations migrate

			期间报错：
				'
				ERRORS:
				users.UserProfile.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
					HINT: Get Pillow at https://pypi.python.org/pypi/Pillow or run command "pip install Pillow"
				'
				解决办法：pip install Pillow

				
				django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001\_initial is applied before its dependency users.0001\_initial on database 'default'.
				其实这个问题就是你之前已经定义了userProfile并且还设置了重载它的语句，现在又来定义它，它是不会再给你提供那么多的初始表的：
				所以我们需要删除除了auth_user以外的其他表，如果一次删除不了（那是因为表与表之间存在外键联系）就一个个的删除：

				**注意一下**

				我们以后不要在初始化的时候就执行makemigrations & migrate操作，应当在我们设计完userProfile（自定义字段）之后再执行该操作，那样就不会报错了。

## 循环引用 ##

	![循环引用图片](https://i.imgur.com/ViOOaXT.png)

	我们通常会在user中定义userCourse这个字段，用来记录用户学习的课程，它会有两个外键：user和course。所以在用到的时候，我们需要import Courses.models。
	
	同样，如果用户对于某个课程需要评论，那么我们需要定义CourseComment这个字段，而且它肯定会放在 Courses.models当中。所以在用到的时候，我们又需要import User.models。
	
	这是只有2个app的情况，当还有更多的情况：3个，4个，5个...apps时，循环调用import会出错导致系统不能正确识别，而且最起码会造成时间上的等待。那么有没有好的方法来解决这个问题呢？答案是有的！可以采用分层设计的思想来解决这个难题。
	分层设计
	
	在前面的第六篇笔记中我们已经说过，准备新建4个app,其中的3个apps:
	 **(users)用户版块**,**(course)课程版块**,**(organization)授课教师与授课机构板块**, 就是一些常规的信息存储，而第4个**(operation)用户操作板块**就是采用分层设计的思想来设计的，而且我们保证**operation**这个app的优先级高于其他3个，所以可以随时import这些底层的apps。各个apps的层级关系如下图所示：
	
	![app分层](https://i.imgur.com/Ux0yTlD.png)

	在users这个app中，我们自定义了UserProfile这个表用来覆盖系统默认的user表。这样其实我们这个users应用已经设计完了。不过呢，通过研究我们发现有些功能是非常独立的，我们为了平衡一些app的代码量，可以将它们放在这个users项目里面。

    EmailVerifyRecord - 邮箱验证码
    Banner - 轮播图

	邮箱验证码的设计
	
	验证码分三种类型，分别用于不同的功能：注册；找回密码；修改邮箱，所以在设计验证码类型的时候注意选择的条件，通常验证码包括这些字段：code,email,send\_type,send\_time。
	
	我们打开users/models.py文件，接着之前的代码在后面添加如下内容:

		'
		'''
		邮箱验证码
		'''
		class EmailVerifyRecord(models.Model):
		    code = models.CharField(max_length=20, verbose_name="验证码")
		    email = models.EmailField(max_length=50, verbose_name="邮箱")
		    send_type = models.CharField(verbose_name="验证码类型", choices=(('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')), max_length=30)
		    # 这里的now得去掉(),如果不去掉则会根据编译时间，而不是我们要的实例化时间。
		    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)
		
		    class Meta:
		        verbose_name = "邮箱验证码"
		        verbose_name_plural = verbose_name
		
		    def __str__(self):
		        return self.email
		'

	轮播图的设计

	轮播图是一个可以自动切换图片的效果，它包括标题，具体的图片，点击图片后的跳转地址，图片的轮播顺序，添加时间等要素：title,image,url,index,add\_time。
	
	我们打开users/models.py文件，接着之前的代码在后面添加如下内容:

	'
	'''
	轮播图
	'''
	class Banner(models.Model):
	
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
	'

	你可能会问，为什么不把与用户相关的评论，点赞，学习的课程，课程进度等信息也放到这个app中呢？其实是因为那些信息的相关性很大，经常是循环引用，所以我们把那些信息都放到operation这个app中。

## 数据库字段的定义2 ##
	*course 课程模块
		创建courses app

			创建 课程信息 Course model
			'
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
			'		
		
		创建 章节信息 Lesson model

			'
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
			        # return self.name也是可以
			'
			外键参数解释：
				*course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")，
				这其实就是一个用于告知信息的字段，包含3个参数：Course是指你与哪个对象存在外键关系（记住是表的名称，不是字段的名称）；
				on_delete=models.CASCADE是指主外关系键中，级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除；	*

		创建 视频信息 Video model

			'
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
			        return '<<{0}>>章节的视频》{1}'.format(self.lesson, self.name)   # return self.name也是可以

			'
			
		创建 课程资料信息 courseResource model

			'
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
			        return '<<{0}>>课程的课程资料》{1}'.format(self.course, self.name)   # return self.name也行
			'

	*organization 课程模块
		创建organization app

		创建 CityDict、CourseOrg、Teacher model

		'
		from django.db import models
		from datetime import datetime
		# Create your models here.
		# 城市信息
		class CityDict(models.Model):
		    name = models.CharField(max_length=20, verbose_name="城市")
		    # 描述这一块，我们先用TextField，因为它允许我们不输入长度,而且可以输入值无范围，之后再更新为富文本形式
		    desc = models.CharField(max_length=200, verbose_name="描述")
		    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
		
		    class Meta:
		        verbose_name = "城市"
		        verbose_name_plural = verbose_name
		
		    def __str__(self):
		        return self.name   # 这里很重要，否则在后台就显示不出Meta信息
		
		
		# 课程机构
		class CourseOrg(models.Model):
		    name = models.CharField(max_length=50, verbose_name="机构名称")
		    desc = models.TextField(verbose_name="机构描述")
		    tag = models.CharField(max_length=10, default="全国知名", verbose_name="机构标签")
		    category = models.CharField(max_length=20, default='pxjg',
		choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')), verbose_name="机构类别")
		    click_nums = models.IntegerField(default=0, verbose_name='点击数')
		    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
		    image = models.ImageField(max_length=50, upload_to="org/%Y/%m", verbose_name="logo")
		    address = models.CharField(max_length=150, verbose_name="机构地址")
		    # 前面知道一个城市对应多个课程机构，所以在课程机构表中将城市设置为外键。
		    # 此处的city其实就是一个用来告诉我们这个课程机构属于哪个城市的字段
		    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name="所在城市说明")
		    students = models.IntegerField(default=0, verbose_name="学习人数")
		    course_nums = models.IntegerField(default=0, verbose_name="课程数")
		    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
		
		    class Meta:
		        verbose_name = "课程机构"
		        verbose_name_plural = verbose_name
		
		    def __str__(self):
		        return self.name   # 这里很重要，否则在后台就显示不出Meta信息
		
		
		# 教师信息
		class Teacher(models.Model):
		    # 前面知道一个课程机构对应多个教师，所以在教师信息表中将授课机构设置为外键。
		    # 此处的org其实就是一个用来告诉我们这个教师属于哪个课程机构的字段
		    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属教师")
		    name = models.CharField(max_length=50, verbose_name="教师名")
		    work_years = models.IntegerField(default=0, verbose_name="工作年限")
		    work_position = models.CharField(max_length=50, verbose_name="公司职位")
		    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    		course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE, null=True, blank=True)#这个可以以后在加
		    points = models.CharField(max_length=50, verbose_name="教学特点")
		    click_nums = models.IntegerField(default=0, verbose_name="点击数")
		    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
		    age = models.IntegerField(default=18, verbose_name='年龄')
		    image = models.ImageField(default='', upload_to='teacher/%Y/%m',
		verbose_name='头像', max_length=100)
		    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
		
		    class Meta:
		        verbose_name = "教师"
		        verbose_name_plural = verbose_name
		
		    def __str__(self):
		        return self.name   # 这里很重要，否则在后台就显示不出Meta信息
		'

		

	*operation 课程模块
		创建operation app

		创建  UserAsk、CourseComments、UserFavorite、UserMessage、UserCourse model

		'
		from django.db import models
		from datetime import datetime
		# Create your models here.
		
		from users.models import UserProfile
		from courses.models import Course
		
		
		# 用户我要学习信息
		class UserAsk(models.Model):
		    name = models.CharField(max_length=20, verbose_name="姓名")
		    mobile = models.CharField(max_length=11, verbose_name="手机")
		    course_name = models.CharField(max_length=50, verbose_name="课程名")
		    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
		
		    class Meta:
		        verbose_name = "用户咨询"
		        verbose_name_plural = verbose_name
		
		    def __str__(self):
		        return self.name    # 这里很重要，否则在后台就显示不出Meta信息
		
		
		# 课程评论
		class CourseComments(models.Model):
		    # 前面知道一个用户发表多个课程评论，所以在课程评论表中将用户设置为外键。
		    # 此处的user其实就是一个用来告诉我们这个课程评论属于哪个用户的字段
		    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户名")
		    # 前面知道一门课程具有多个课程评论，所以在课程评论表中将课程设置为外键。
		    # 此处的course其实就是一个用来告诉我们这个课程评论属于哪个课程的字段
		    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
		    comment = models.CharField(max_length=200, verbose_name="评论")
		    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
		
		    class Meta:
		        verbose_name = '课程评论'
		        verbose_name_plural = verbose_name
		
		    def __str__(self):
		        return self.comment   # 这里很重要，否则在后台就显示不出Meta信息
		
		
		# 用户收藏信息
		class UserFavorite(models.Model):
		    # 前面知道一个用户可以收藏多个内容，所以在用户收藏表中将用户设置为外键。
		    # 此处的user其实就是一个用来告诉我们这个用户收藏属于哪个用户的字段
		    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户名")
		    fav_id = models.IntegerField(default=0, verbose_name='数据Id')
		    fav_type = models.CharField(choices=(('1', '课程'), ('2', '课程机构'), ('3', '讲师')), default=1,
		verbose_name='收藏类型',max_length=2)
		    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
		
		    class Meta:
		        verbose_name = "用户收藏"
		        verbose_name_plural = verbose_name
		
		    def __str__(self):
		        return self.user   # 这里很重要，否则在后台就显示不出Meta信息
		
		
		# 用户消息信息
		class UserMessage(models.Model):
		    # 我们的消息有两种:一种是发给全员，另一种则是发给特定某一个用户。
		    # 所以如果使用外键，那么每个消息就要对应一个用户，比较难以实现全员消息的通知。
		    # 因此我们设置用户id,如果为0就发给所有用户，不为0就是发给特定Id的用户。
		    user = models.IntegerField(default=0, verbose_name="接收用户")
		    message = models.CharField(max_length=500, verbose_name='消息内容')
		    # 设置消息是否已读，采用布尔类型 BooleanField： False表示未读,True表示已读。
		    has_read = models.BooleanField(default=False, verbose_name='是否已读')
		    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
		
		    class Meta:
		        verbose_name = '用户消息'
		        verbose_name_plural = verbose_name
		
		    def __str__(self):
		        return self.message  # 这里很重要，否则在后台就显示不出Meta信息
		
		
		# 用户课程信息
		class UserCourse(models.Model):
		    # 前面知道一个用户可以学习多门课程，所以在用户课程表中将用户设置为外键。
		    # 此处的user其实就是一个用来告诉我们这个课程属于哪个用户的字段
		    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户名')
		    # 前面知道一门课程可以有多个课程的信息，所以在用户课程表中将课程设置为外键。
		    # 此处的course其实就是一个用来告诉我们这个课程信息属于哪门课程的字段
		    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
		    add_time = models.DateTimeField(default=datetime.now, verbose_name='学习时间')
		
		    class Meta:
		        verbose_name = '用户课程'
		        verbose_name_plural = verbose_name
		
		        def __str__(self):
		            return self.user  # 这里很重要，否则在后台就显示不出Meta信息
		'

## django自带admin与xadmin ##

	*设置后台语言与市区

		'
		# 将语言修改为中文
		LANGUAGE_CODE = 'zh-hans'
		
		# 将时区修改为上海
		TIME_ZONE = 'Asia/Shanghai'
		
		# 数据库存储使用时间，True时间会被存为UTC的时间。所以采用False
		USE_TZ = False
		'

	*注册model到后台
		model需要再admin.py中注册才能在后台显示
		以userProfile为例
		'
		from django.contrib import admin

		# Register your models here.
		from users.models import UserProfile
		
		admin.site.register(UserProfile)
		'

	*安装xadmin

		xadmin对于django2支持不好，找了一个修改好的版本可以直接使用，存在了百度网盘https://pan.baidu.com/s/1DoXyFn2_g2_RQVPorjhp1w

		新建一个名为extra_apps的Python package ,用来存放我们的第三方插件，并将前面下载的xadmin文件（解压之后）移入其中：

		同时需要对路径进行配置：打开eduline/settings.py文件，找到里面的第16行代码，我们加入以下内容：
		
		'import os, sys
		
		# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
		sys.path.insert(0,os.path.join(BASE_DIR, 'extra_apps'))'
		
		接下来是xadmin的安装:在确保前面的操作完成以后，我们打开eduline/settings.py文件，找到里面的第35行代码，在后面修改为如下：
		
		'INSTALLED\_APPS = [
		
		'django.contrib.admin',
		
		'django.contrib.auth',
		
		'django.contrib.contenttypes',
		
		'django.contrib.sessions',
		
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'users',
		'courses',
		'organization',
		'operation',
		'xadmin',
		'crispy_forms'
		]'
		
		然后打开eduline/urls.py文件，把urls中默认的admin修改为xadmin:
		
		'from django.urls import path
		
		import xadmin
		
		urlpatterns = [
		path('xadmin/', xadmin.site.urls),
		
		]'
		
		然后进行我们数据库的生成和迁移操作：makemigrations和migrate：
		
		你会发现执行第一个命令就报错了，那是因为我们缺少一些库的支持，我们依次按照如下库：
		
		pip install future
		
		pip install six
		
		pip install httplib2
		
		pip install django-import-export
		
		pip install django-formtools==2.1   # 记住一定是2.1的版本，否则会出错
		
		使用的命令为：pip install package -i https://pypi.tuna.tsinghua.edu.cn/simple
		
		之后会安装一大堆库，我们使用pip list命令查看一下：
		
		为了便于你查看自己是否缺少某个库，我这里贴一下我的各个库的版本（你各个库的版本不能低于我的版本，否则就可能会出错）：
	
		接下来，我们重新进行数据库的生成和迁移操作：makemigrations和migrate,现在xadmin的配置已经完成了.
		
	
	*Xadmin的使用介绍

		正如前面你所知道的，Xadmin是基于Django的admin来开发的，所以Xadmin也继承了许多admin的用法，下面就分别介绍一下它们的使用情况：
		
		因为我们之前在admin里面已经注册了UserProfile，所以xadmin里面也就有了这个信息，那我们接下来就设置一下我们文件的格式，让系统默认去寻找我们xadmin的adminx.py文件，而不是去寻找原来admin的admin.py文件。
		验证码功能的实现
		
		我们打开eduline/apps/users这个文件夹，在里面新建一个名为adminx.py的文件，我们准备开始验证码功能的实现,在其中添加如下代码：
		
		'#！/user/bin/python
		
		# -_- coding:utf-8 -_-
		
		# @Time: 2018/3/26 10:05
		
		# @Author: Envse
		
		# @File: adminx.py
		
		# 导入xadmin，如果出现字体底下出现红色属于正常现象（实际上环境已经配置过）
		
		import xadmin
		
		# 因为处于同一个目录之下，所以可以直接使用.models代替当前目录
		
		from .models import EmailVerifyRecord
		
		# 写一个管理器，命名规则：Model+Admin,注意这里不再是继承admin，而是继承object这个最高类
		
		class EmailVerifyRecordAdmin(object):
		
		pass
		
		# 将EmailVerifyRecord注册进我们的admin中, 并为它选择管理器EmailVerifyRecordAdmin
		
		xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)'

		现在xadmin后台就添加上了 邮箱验证码的model

		现在想在后台页面同时显示全部model字段信息，所以需要配置一下:我们打开users/adminx.py文件，在里面的管理器中设置list_display字段:


		'
		# 写一个管理器，命名规则：Model+Admin,注意这里不再是继承admin，而是继承object这个最高类
		
		class EmailVerifyRecordAdmin(object):
		
		# 配置后台显示的列信息
		
		list\_display = 'code', 'email', 'send\_type', 'send\_time'  # 一次显示你想出现的多行数据，
		
		# 这里面的字段都是你在前面数据库中定义的，请保持数据的一致

		'

		然后还可以配置过滤器 search_fields，搜索框 list_filter

		'
		# 写一个管理器，命名规则：Model+Admin,注意这里不再是继承admin，而是继承object这个最高类

		class EmailVerifyRecordAdmin(object):
		
		# 配置后台显示的列信息
		
		list_display = 'code', 'email', 'send_type', 'send_time'  # 一次显示你想出现的多行数据
		
		search_fields = 'code', 'email', 'send_type'  # 查询你想要的数据,一般不依据时间进行查询
		
		list_filter = 'code', 'email', 'send_type', 'send_time'  # 过滤器
		'
		之后刷新一下网页:
		![](https://i.imgur.com/fBnnGAa.png)
		
		*admin, xadmin和其他后台管理系统的区别

			像PHP，JAVA等其他语言，它们是按照一个功能模块来进行一个功能设计的。而admin和 xadmin就不一样了，
			它们是对于每张表都可以进行增删改查的管理器，因此我们还可以在增删改查的基础上加上我们自己的后台逻辑，
			完成我们自定义的功能。因此，从某种程度可以说它是不依赖于具体业务的，不管什么系统后台都是由表组成。

		*以在其余的各个表中，都加上这些个功能。
			
			'
			from .models import Banner

			class BannerAdmin(object):
			
			list\_display = 'title', 'image', 'url', 'index', 'add\_time'  # 一次显示你想出现的多行数据
			
			search\_fields = 'title', 'image', 'url', 'index'  # 查询你想要的数据
			
			list\_filter = 'title', 'image', 'url', 'index', 'add\_time'  # 过滤器
			
			xadmin.site.register(Banner, BannerAdmin)
			'
		

			**再次强调一下：这里面的字段都是你前面在数据库中定义的，请保持数据库字段定义的一致性，不要乱写，否则后面会出很大的BUG！**

		*注册其他app的model并设置adminx.py
			
			Django在根据models生成数据库表时报 __init__() missing 1 required positional argument: 'on_delete'
			解决方法：在外键值的后面加上 on_delete=models.CASCADE 原文链接https://www.cnblogs.com/phyger/p/8035253.html
			
			courses
				'
				import xadmin
				from .models import *
				
				
				class CourseAdmin(object):
				    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
				                    'add_time']
				    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'image', 'click_nums']
				    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
				                   'add_time']
				
				
				class LessonAdmin(object):
				    list_display = ['course', 'name', 'add_time']
				    search_fields = ['course', 'name']
				    list_filter = ['course', 'name', 'add_time']
				
				
				class VideoAdmin(object):
				    list_display = ['lesson', 'name', 'add_time']
				    search_fields = ['lesson', 'name']
				    list_filter = ['lesson', 'name', 'add_time']
				
				
				class CourseResourceAdmin(object):
				    list_display = ['course', 'name', 'download', 'add_time']
				    search_fields = ['course', 'name', 'download']
				    list_filter = ['course', 'name', 'download', 'add_time']
				
				
				xadmin.site.register(Course, CourseAdmin)
				xadmin.site.register(Lesson, LessonAdmin)
				xadmin.site.register(Video, VideoAdmin)
				xadmin.site.register(CourseResource, CourseResourceAdmin)
	
				'
		
			opreation
				'
				import xadmin
				from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse
				
				
				class UserAskAdmin(object):
				    list_display = ['name', 'course_name', 'mobile', 'add_time']
				    search_fields = ['name', 'course_name', 'mobile']
				    list_filter = ['name', 'course_name', 'mobile', 'add_time']
				
				
				class CourseCommentsAdmin(object):
				    list_display = ['user', 'course', 'comment', 'add_time']
				    search_fields = ['user', 'course', 'comment']
				    list_filter = ['user', 'course', 'comment', 'add_time']
				
				
				class UserFavoriteAdmin(object):
				    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
				    search_fields = ['user', 'fav_id', 'fav_type']
				    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
				
				
				class UserMessageAdmin(object):
				    list_display = ['user', 'message', 'has_read', 'add_time']
				    search_fields = ['user', 'message', 'has_read']
				    list_filter = ['user', 'message', 'has_read', 'add_time']
				
				
				class UserCourseAdmin(object):
				    list_display = ['user', 'course', 'add_time']
				    search_fields = ['user', 'course']
				    list_filter = ['user', 'course', 'add_time']
				
				
				xadmin.site.register(UserAsk, UserAskAdmin)
				xadmin.site.register(CourseComments, CourseCommentsAdmin)
				xadmin.site.register(UserFavorite, UserFavoriteAdmin)
				xadmin.site.register(UserMessage, UserMessageAdmin)
				xadmin.site.register(UserCourse, UserCourseAdmin)

				'

			organization

				'
				import xadmin
				from .models import CityDict, CourseOrg, Teacher
				
				
				class CityDictAdmin(object):
				    list_display = ['name', 'desc', 'add_time']
				    search_fields = ['name', 'desc']
				    list_filter = ['name', 'desc', 'add_time']
				
				
				class CourseOrgAdmin(object):
				    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
				    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
				    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
				
				
				class TeacherAdmin(object):
				    list_display = ['name', 'work_years', 'work_company', 'work_position', 'course', 'points', 'click_nums', 'fav_nums',
				                    'add_time']
				    search_fields = ['name', 'work_yesars', 'work_company', 'work_position', 'course', 'points', 'click_nums',
				                     'fav_nums', ]
				    list_filter = ['name', 'work_years', 'work_company', 'work_position', 'course', 'points', 'click_nums', 'fav_nums',
				                   'add_time']
				
				
				xadmin.site.register(CityDict, CityDictAdmin)
				xadmin.site.register(CourseOrg, CourseOrgAdmin)
				xadmin.site.register(Teacher, TeacherAdmin)
				'

## 后台管理配置 ##

	*开启主题功能
		在users/adminx.py中添加
		'
		from .models import EmailVerifyRecord
		
		class BaseSetting(object):
		    enable_themes = True  # 可修改主题
		    use_bootswatch = True  # 增加主题的可选内容
		    
		# 将全局配置管理与view进行绑定
		xadmin.site.register(views.BaseAdminView, BaseSetting)
		'
	
	*后台管理名称配置
		在users/adminx.py中添加
		'
		class GlobalSettings(object):
		    site_title = '测试后台'  # 站点标题
		    site_footer = '测试footer'   # 站点尾注
		    menu_style = 'accordion'   # 折叠收起菜单
		
		# 将站点标题与站点尾注进行注册:
		xadmin.site.register(views.CommAdminView, GlobalSettings)
		'

	*配置apps的后台显示（列表的中文显示）

		打开每个app下面的apps.py文件，追加verbose_name信息。我们以users/apps.py为例,修改为如下：

		'
		from django.apps import AppConfig
		class UsersConfig(AppConfig):
		    name = 'users'
		    verbose_name = '用户信息'
		'
		在每个app的__init__.py文件中添加：
			'default_app_config = "users.apps.UsersConfig"'按此格式添加appname.apps.AppnameConfig（注意第二个Appname首字母大写）

	*自定义菜单显示顺序（未实现太麻烦以后再看）
		记住这段代码是和我们之前定义全局配置放在同一个函数里面的
		
		在users/adminx.py文件加上以下代码：

		'
		from users.models import EmailVerifyRecord, Banner, UserProfile
		from courses.models import Course, CourseResource, Lesson, Video
		from organization.models import CourseOrg, CityDict, Teacher
		from operation.models import CourseComments, UserMessage, UserFavorite, UserCourse, UserAsk
		from django.contrib.auth.models import Group, Permission
		from xadmin.models import Log
		
		
		class GlobalSettings(object):
		    site_title = '慕学后台管理系统'
		    site_footer = '慕海学习网'
		    menu_style = 'accordion'
		
		    def get_site_menu(self):
		        return (
		                {'title': '课程管理', 'menus': (
		                    {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
		                    {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
		                    {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
		                    {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
		                    {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
		                )},
		                {'title': '机构管理', 'menus': (
		                    {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
		                    {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
		                    {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
		                )},
		                {'title': '用户管理', 'menus': (
		                    {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
		                    {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
		                    {'title': '用户课程', 'url': self.get_model_url(UserCourse, 'changelist')},
		                    {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
		                    {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
		                )},
		
		                {'title': '系统管理', 'menus': (
		                    {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
		                    {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
		                    {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
		                    {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
		                    {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
		            )},)
		
		xadmin.site.register(views.CommAdminView, GlobalSettings)
		'
	
	*其他设置
		
		xadmin管理员详情页面布局，导航图标设置：https://www.cnblogs.com/adc8868/p/7506973.html
	


## 首页显示与登录页面的配置 ##

		*拷贝首页文件index.html设置静态页面的url路由
			'	
			from django.views.generic import TemplateView
		    # 用''指代根目录，TemplateView.as_view可以将template转换为view
		    path('', TemplateView.as_view(template_name='index.html'), name='index'),
			'
			
			拷贝静态文件，修改页面中的静态文件链接，目前直接修改为/static/js 或/static/css

		*拷贝首页文件login.html设置静态页面的url路由，修改页面/static/js 或/static/css，修改首页的login连接。
			path('login/', TemplateView.as_view(template_name="login.html"), name="login"
			
			
		*视图函数View的创建

			'
			# 当我们配置的url被这个view处理时，将会自动传入request对象.
			def user_login(request):
			    # 前端向后端发送的请求方式有两种: get和post
			
			    # 登录提交表单时为post
			    if request.method == "POST":
			        pass
			    # 获取登录页面时为get
			    elif request.method == "GET":
			        # render的作用是渲染html并返回给用户
			        # render三要素: request ，模板名称 ，一个字典用于传给前端并在页面显示
			        return render(request, "login.html", {})
			'

			修改login.html中的from action连接 并在form中添加 {% csrf_token %}
			
		*使用django的默认认证机制（账号密码）

			'
			# 登录提交表单时为post
		    if request.method == "POST":
		        # username，password为前端页面name的返回值，取到用户名和密码我们就开始进行登录验证;取不到时为空。
		        user_name = request.POST.get('username', '')
		        pass_word = request.POST.get('password', '')
		        user = authenticate(username=user_name, password=pass_word)
		        if user is not None:
		            # login 有两个参数：request和user。我们在请求的时候，request实际上是写进了一部分信息，
		            # 然后在render的时候，这些信息也被返回前端页面从而完成用户登录。
		            login(request, user)
		            # 页面跳转至网站首页 user request也会被带回到首页，显示登录状态
		            return render(request, 'index.html')
		        else:
		            # 说明里面的值是None，再次跳转回主页面并报错
		            return render(request, "login.html", {})
			'

			**注意： authenticate的调用只需要传入用户名和密码即可，如果成功则会返回user对象，失败就返回null**

			html页面登录验证配置
	
				'
				{% if request.user.is_authenticated %}   
	                <div class="top">
					<div class="wp">
						<div class="fl"><p>服务电话：<b>33333333</b></p></div>
	                    <!--登录后跳转-->
	
							<div class="personal">
	                            <dl class="user fr">
	                                <dd>admin@admin.com<img class="down fr" src="/static/images/top_down.png"/></dd>
	                                <dt><img width="20" height="20" src="/static/media/image/2016/12/default_big_14.png"/></dt>
	                            </dl>
	                            <div class="userdetail">
	                            	<dl>
		                                <dt><img width="80" height="80" src="/static/media/image/2016/12/default_big_14.png"/></dt>
		                                <dd>
		                                    <h2>管理员</h2>
		                                    <p>admin@admin.com</p>
		                                </dd>
	                                </dl>
	                                <div class="btn">
		                                <a class="personcenter fl" href="usercenter-info.html">进入个人中心</a>
		                                <a class="fr" href="/logout/">退出</a>
	                                </div>
	                            </div>
	                        </div>
	
					</div>
				</div>    <!--如果用户登录成功，显示个人中心-->
	            {% else %}             
	                <div class="top">
					<div class="wp">
						<div class="fl"><p>服务电话：<b>33333333</b></p></div>
	                        <a style="color:white" class="fr registerbtn" href="register.html">注册</a>
	                        <a style="color:white" class="fr loginbtn" href="/login/">登录</a>
	
	                </div>
	            </div>    <!--如果用户登录失败，显示用户登录按钮-->
	            {% endif %}
				'
		*使用邮箱登录

			
			打开eduline/settings.py文件，在第34行添加如下代码：
			'
			AUTHENTICATION_BACKENDS = (
			    'users.views.CustomBackend',
			)'
			
			然后打开users/views.py文件，在后面添加如下代码：
			'
			from django.contrib.auth.backends import ModelBackend
			from .models import UserProfile
			# Q是并集运算
			from django.db.models import Q
			
			# 实现用户名邮箱均可登录的函数，必须继承ModelBackend类，因为它有方法authenticate
			class CustomBackend(ModelBackend):
			    def authenticate(self, username=None, password=None, **kwargs):
			        try:
			 # 我们不希望用户存在两个，也就是说通过某个用户名和某个邮箱登录的都是指向同一用户，所以采用Q来进行并集查询
			            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
			
			            # 记住不能使用password==password，因为密码都被django的后台给加密了
			
			            # UserProfile继承的AbstractUser中有check_password这个函数
			            if user.check_password(password):
			                return user
			        except Exception as e:
			            return None
			'
			但是错误信息如何在前端页面显示呢？我们需要配置一下,打开login.html文件，找到第80行代码：
			'
			<div class="error btns login-form-tips" id="jsLoginTips"></div>
			
			这个字段就是用来提示错误信息的，我们修改一下：
			
			<div class="error btns login-form-tips" id="jsLoginTips">{{ msg }}</div>
			'