from django.shortcuts import render
from users import models as UserModels
from courses import models as CoursesModels
from django.db.models import Q
from courses.get_data_filtered_models import Courses as GetAvailableObjects
from users.user_conditions_and_short_data_returns.user_conditions1 import is_user_authenticated
from users.user_conditions_and_short_data_returns import user_return_data

def search_courses(request):
    course_id = request.GET.get("course_id")
    if course_id == "all":
        course_id = GetAvailableObjects.get_available_all_objs(CoursesModels.Courses.objects.all()).values_list("id",flat=True)
    else:
        course_id = [course_id]
    category_id = request.GET.get("category_id")
    search_text = request.GET.get("search_text")
    course_objects = GetAvailableObjects.get_available_all_objs(CoursesModels.Courses.objects.filter(Q(name__icontains=search_text)| Q(category__name=search_text)).filter(id__in=course_id)).order_by("-id")
    return_data = {"courses_data":course_objects}
    return render(request,'courses/searched_result.html',return_data)

def view_course(request):
    course_id = request.GET.get("course_id")
    course_objects = GetAvailableObjects.get_available_last_obj(CoursesModels.Courses.objects.filter(id=course_id))
    Course_Images = CoursesModels.CourseImages.objects.filter(course_id=course_id)
    return_data = {"courses_data":course_objects,'CourseImages':Course_Images}

    return render(request,'courses/view_course.html',return_data)

def download_course_detail_file(request):
    if request.user.is_authenticated:
        user_obj = request.user
    course_id = request.GET.get("course_id")

    courses_obj = GetAvailableObjects.get_available_last_obj(CoursesModels.Courses.objects.filter(id=course_id))

    courses_obj.CourseFile

def create_zoom_meeting(request):
    import jwt
    import requests
    import json
    from time import time

    # Enter your API key and your API secret
    API_KEY = 'Your API key'
    API_SEC = 'Your API secret'

    # create a function to generate a token
    # using the pyjwt library

    def generateToken():
        API_KEY = "RYmtYftgTYSZKoFrlVtnqQ"
        API_SEC = "yXPW7yTThyQ45ALiOmM0wl4AvRaAXxQsSllk"
        apitoken = "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDVkgwdnhPTFNVS0NFdGZTckZmdDNRIn0.kBG95ef2SabJ2zQL7pR8wb-qjgEUOyq87sSc89wpjHM"
        token = jwt.encode(

            # Create a payload of the token containing
            # API Key & expiration time
            {'iss': API_KEY, 'exp': time() + 5000},

            # Secret used to generate token signature
            API_SEC,

            # Specify the hashing alg
            algorithm='HS256'
        )
        return token.decode('utf-8')

    # create json data for post requests
    meetingdetails = {"topic": "The title of your zoom meeting",
                      "type": 2,
                      "start_time": "2019-06-14T10: 21: 57",
                      "duration": "45",
                      "timezone": "Europe/Madrid",
                      "agenda": "test",

                      "recurrence": {"type": 1,
                                     "repeat_interval": 1
                                     },
                      "settings": {"host_video": "true",
                                   "participant_video": "false",
                                   "join_before_host": "False",
                                   "mute_upon_entry": "False",
                                   "watermark": "true",
                                   "audio": "voip",
                                   "auto_recording": "cloud"
                                   }
                      }

    # send a request with headers including
    # a token and meeting details

    def createMeeting():
        headers = {'authorization': 'Bearer ' + generateToken(),
                   'content-type': 'application/json'}
        r = requests.post(
            f'https://api.zoom.us/v2/users/me/meetings',
            headers=headers, data=json.dumps(meetingdetails))

        print("\n creating zoom meeting ... \n")
        # print(r.text)
        # converting the output into json and extracting the details
        y = json.loads(r.text)
        join_URL = y["join_url"]
        meetingPassword = y["password"]

        print(
            f'\n here is your zoom meeting link {join_URL} and your \
    		password: "{meetingPassword}"\n')

    # run the create meeting function
    createMeeting()
    return None


from courses.Certivificates import first_certivificates
def get_certivificate(request):

    return first_certivificates

def user_courses(request):
    if is_user_authenticated(request):
        user = user_return_data.login_user(request)
        registerd_courses = CoursesModels.CourseRegister.objects.filter(user=user)
        paid_enrolled_courses = CoursesModels.FeeDetails.objects.filter(user=user)
        context = {"registerd_courses":registerd_courses,"paid_enrolled_courses":paid_enrolled_courses}
        return render(request,"users/user_courses.html",context=context)
    else:
        return user_return_data.login_page(request)

def register_courses(request):
    if is_user_authenticated(request):
        course_id = request.POST.get("course_id")
        user = user_return_data.login_user(request)
        create,get_course = CoursesModels.CourseRegister.objects.get_or_create(user=user,course_id=course_id,added_by=user)
        return view_course(request)
    else:
        return user_return_data.login_page(request)