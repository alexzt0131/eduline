import xadmin

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




xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

