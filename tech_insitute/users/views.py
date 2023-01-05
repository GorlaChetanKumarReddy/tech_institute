from django.shortcuts import render
from users import models as UserModels
from courses import models as CoursesModels
import datetime

# from courses import courses_data_functions as CoursesData



def Main_Page(request):
    five_days_from =  (datetime.datetime.now() - datetime.timedelta(days=7)).date()
    main_images = CoursesModels.MainImages.objects.filter(is_active=True).order_by("-id")
    courses_data = CoursesModels.Courses.objects.filter(is_active=True,start_date__gte=five_days_from).order_by("-id")
    data = {"data":courses_data,"main_images":main_images}
    return render(request,'users/index.html',data)
