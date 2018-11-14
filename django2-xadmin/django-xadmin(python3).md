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


## 数据库字段的定义 ##
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