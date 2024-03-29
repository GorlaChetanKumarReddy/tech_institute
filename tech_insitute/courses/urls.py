"""tech_insitute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from courses import views

urlpatterns = [
    path('search_courses/',views.search_courses,name='search_courses'),
    path('my_course_certivificate/',views.get_certivificate,name='my_course_certivificate'),
    path('view_course/',views.view_course,name='view_course'),
    path('download_course_detail_file/',views.download_course_detail_file,name='download_course_detail_file'),
    path('register_courses/', views.register_courses, name="register_courses"),
    path('user_courses/', views.user_courses, name="user_courses"),
]
