from django.shortcuts import render
from users import models as UserModels
from courses import models as CoursesModels

from courses import courses_data_functions as CoursesData



def Main_Page(request):
    data = {"data":[CoursesData]}
    return render(request,'users/index.html',data)
