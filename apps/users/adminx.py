

import xadmin


from .models import EmailVerifyRecord,Banner

from xadmin import views


class EmailVerifyRecordAdmin(object):
    list_display = ['code','eamil','send_type','send_time']
    search_fields = ['code','eamil','send_type']
    list_filter = ['code','eamil','send_type','send_time']


class BannerAdmin(object):

    list_display = ['title','image','url','index','add_tiem']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_tiem']


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '晨霜'
    site_footer = '此生谁料，心在天山，身老沧州'
    menu_style = 'accordion'

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)