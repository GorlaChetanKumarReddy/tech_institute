from django.contrib import admin
from courses import models as CoursesModels






admin.site.register(CoursesModels.Courses)
admin.site.register(CoursesModels.CoursesCategory)
admin.site.register(CoursesModels.CourseImages)
admin.site.register(CoursesModels.MainImages)
