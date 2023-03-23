from django.shortcuts import render
from users import models as UserModels
from courses import models as CoursesModels
from django.db.models import Q

def get_available_last_obj(objs):
    return objs.filter(is_active=True).last()

def get_available_all_objs(objs):
    return objs.filter(is_active=True)


