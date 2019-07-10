from .models import Course,Lesson,Video,CourseResourse

import xadmin

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','student','fav_num','image','click_nums','add_time']
    search_fields = ['name','desc','detail','degree','learn_times','student','fav_num','image','click_nums','add_time']
    list_filter = ['name','desc','detail','degree','learn_times','student','fav_num','image','click_nums','add_time']


class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__name','name','add_time']

class VideoAdmin(object):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson__name','name','add_time']

class CourseResourseAdmin(object):
    list_display = ['course', 'name', 'add_time','download']
    search_fields = ['course', 'name','download']
    list_filter = ['course', 'name', 'add_time','download']



xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResourse,CourseResourseAdmin)