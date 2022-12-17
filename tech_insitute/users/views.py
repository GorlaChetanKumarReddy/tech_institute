from django.shortcuts import render
from users import models as UserModels
from courses import models as CoursesModels

# from courses import courses_data_functions as CoursesData



def Main_Page(request):
    main_images = CoursesModels.MainImages.objects.filter(is_active=True)
    courses_data = CoursesModels.Courses.objects.filter(is_active=True)
    data = {"data":courses_data,"main_images":main_images}
    return render(request,'users/index.html',data)
