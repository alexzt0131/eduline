import xadmin
from xadmin import views

from .models import EmailVerifyRecord
from .models import Banner


class EmailVerifyRecordAdmin(object):

    list_display = ['code', 'email', 'send_type', 'send_time']

    search_fields = ['code', 'email', 'send_type']

    list_filter = ['code', 'email', 'send_type', 'send_time']




class BannerAdmin(object):

    list_display = 'title', 'image', 'url', 'index', 'add_time'  # 一次显示你想出现的多行数据

    search_fields = 'title', 'image', 'url', 'index'  # 查询你想要的数据

    list_filter = 'title', 'image', 'url', 'index', 'add_time'  # 过滤器



class BaseSetting(object):

    enable_themes = True    #可修改主题
    use_bootswatch = True   #增加主题的可选内容


class GlobalSettings(object):

    site_title = '测试后台'  # 站点标题
    site_footer = '测试footer'   # 站点尾注
    menu_style = 'accordion'   # 折叠收起菜单


# 将站点标题与站点尾注进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)

#将全局配置管理与view进行绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)



xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

