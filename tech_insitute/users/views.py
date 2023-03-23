from django.shortcuts import render
from users import models as UserModels
from courses import models as CoursesModels
import datetime
from django.contrib.auth import logout
from users.user_conditions_and_short_data_returns.user_conditions1 import is_user_authenticated
from users.user_conditions_and_short_data_returns import user_return_data
from django.db.models import F, Q, When,Case
# from courses import courses_data_functions as CoursesData

def check_user_enrolled_course_available(Courses):
    user = user_return_data.login_user()
    course_types = CoursesModels.CoursesCategory.objects.all()
    five_days_from = (datetime.datetime.now() - datetime.timedelta(days=30)).date()
    main_images = CoursesModels.MainImages.objects.filter(is_active=True).order_by("-id")
    courses_data = CoursesModels.Courses.objects.filter(start_date__gte=five_days_from).order_by("-id")

    # courses_data.filter(Case(CoursesModels.FeeDetails.objects.get(user=user,course_id=)))

def Main_Page(request):
    course_types = CoursesModels.CoursesCategory.objects.all()
    five_days_from =  (datetime.datetime.now() - datetime.timedelta(days=30)).date()
    main_images = CoursesModels.MainImages.objects.filter(is_active=True).order_by("-id")
    courses_data = CoursesModels.Updated_Courses.objects.filter(start_date__gte=five_days_from).order_by("-id").values_list("id",flat=True).distinct("course")

    data = {"data":courses_data,"main_images":main_images,"course_types":course_types}
    return render(request,'users/index.html',data)

def logout_page(request):
    logout(request)
    return Main_Page(request)


