from django.db import models
from django.contrib.auth.models import User

class MandetoryFields(models.Model):
    added_date_time = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User,on_delete=models.PROTECT)

    class Meta:
        abstract = True

class MainImages(MandetoryFields):
    Image1 = models.ImageField(upload_to="MainImages")
    link = models.URLField(null=True,blank=True)
    is_active = models.BooleanField(default=False)


class CoursesCategory(MandetoryFields):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Courses(MandetoryFields):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(CoursesCategory,on_delete=models.PROTECT)
    image1 = models.ImageField(upload_to="courses_images")
    faculty_name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    start_timing = models.TimeField()
    end_timing = models.TimeField()
    duration_days = models.IntegerField()
    Discription1 = models.TextField()
    Discription2 = models.TextField(null=True,blank=True)
    Discription3 = models.TextField(null=True,blank=True)
    CourseFile = models.FileField(upload_to="CourseFile")
    CourseFile2 = models.FileField(upload_to="CourseFile",null=True,blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (["name"])


class CourseImages(MandetoryFields):
    course = models.OneToOneField(Courses,on_delete=models.CASCADE)
    Image2 = models.ImageField(upload_to="CourseImages")
    Image3 = models.ImageField(upload_to="CourseImages",null=True,blank=True)
    Image4 = models.ImageField(upload_to="CourseImages",null=True,blank=True)



