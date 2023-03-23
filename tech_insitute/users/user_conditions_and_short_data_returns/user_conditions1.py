

def is_user_authenticated(request):
    if request.user.is_authenticated:
        return True
    else:
        return False