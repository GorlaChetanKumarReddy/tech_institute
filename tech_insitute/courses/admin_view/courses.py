from django.contrib import admin
from courses import models as CoursesModels
from django import forms
from courses.get_data_filtered_models import Courses as GetAvailableObjects

class UpdateCourseForm(forms.ModelForm):

    class Meta:
        model = CoursesModels.Updated_Courses
        fields = '__all__'

class UpdateCourseAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        super(UpdateCourseAdmin, self).__init__(model, admin_site)
