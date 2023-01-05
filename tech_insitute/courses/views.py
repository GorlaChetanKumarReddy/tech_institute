from django.shortcuts import render
from users import models as UserModels
from courses import models as CoursesModels
from django.db.models import Q


def search_courses(request):
    course_id = request.GET.get("area")
    if course_id == "all":
        course_id = CoursesModels.Courses.objects.all().values_list("id",flat=True)
    else:
        course_id = [course_id]
    category_id = request.GET.get("category_id")
    search_text = request.GET.get("search_text")
    course_objects = CoursesModels.Courses.objects.filter(Q(name__icontains=search_text)| Q(category__name=search_text)).filter(is_active=True,id__in=course_id).order_by("-id")

    return_data = {"courses_data":course_objects}
    return render(request,'courses/searched_result.html',return_data)


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
