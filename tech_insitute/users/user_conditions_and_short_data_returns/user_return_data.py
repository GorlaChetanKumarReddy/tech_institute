from django.shortcuts import render,redirect


def login_user(requst):
    return requst.user


def login_page(request,message=None):
    context = {"message":message}
    return render(request,'users/login_page.html',context=context)