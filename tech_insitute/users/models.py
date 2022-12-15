from django.db import models
from django.contrib.auth.models import User



class UserMoreDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.BigIntegerField()
    added_date_timm = models.DateTimeField(auto_now_add=True)
