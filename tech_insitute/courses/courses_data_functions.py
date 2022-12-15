from courses import models as CoursesModels


def courses_active_data():
    courses_data = CoursesModels.Courses.objects.filter(is_active=True)

    retun_data = {"courses_data":courses_data}

    return retun_data