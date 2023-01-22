from django.shortcuts import render
from users import models as UserModels
from courses import models as CoursesModels
import datetime
from django.contrib.auth import logout

# from courses import courses_data_functions as CoursesData



def Main_Page(request):
    course_types = CoursesModels.CoursesCategory.objects.all()
    five_days_from =  (datetime.datetime.now() - datetime.timedelta(days=30)).date()
    main_images = CoursesModels.MainImages.objects.filter(is_active=True).order_by("-id")
    courses_data = CoursesModels.Courses.objects.filter(start_date__gte=five_days_from).order_by("-id")
    data = {"data":courses_data,"main_images":main_images,"course_types":course_types}
    return render(request,'users/index.html',data)

def logout_page(request):
    logout(request)
    return Main_Page(request)
