from django.contrib import admin
from courses import models as CoursesModels
from courses.admin_view import courses as CoursesAdmin






admin.site.register(CoursesModels.Courses)
admin.site.register(CoursesModels.Updated_Courses,CoursesAdmin.UpdateCourseAdmin)
admin.site.register(CoursesModels.CoursesCategory)
admin.site.register(CoursesModels.CourseImages)
admin.site.register(CoursesModels.MainImages)
