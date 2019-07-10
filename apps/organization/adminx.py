from .models import City,CourseOrg,Teacher

import xadmin

class CityAdmin(object):
    list_display = ['name','add_time','desc']
    search_fields = ['name','desc']
    list_filter = ['name','add_time','desc']


class CourseOrgAdmin(object):
    list_display = ['name','desc','click_num','fav_num','image','address','city','add_time']
    search_fields = ['name','desc','click_num','fav_num','image','address','city']
    list_filter = ['name','desc','click_num','fav_num','image','address','city','add_time']


class TeacherAdmin(object):
    list_display = ['org','name','work_years','work_company','work_position','points','click_num','fav_num','add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_num', 'add_time']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_num',
                    'add_time']

xadmin.site.register(City,CityAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)