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
    price = models.BigIntegerField(default=0)
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

class CourseRegister(MandetoryFields):
    course = models.ForeignKey(Courses,on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name="course_registerd_user")

    def __str__(self):
        return str(self.course.name)+" | "+str(self.user.first_name)

class PaymentType(MandetoryFields):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    class Meta:
        unique_together = (['name'])

class FeeDetails(MandetoryFields):
    payment_type = models.ForeignKey(PaymentType,on_delete=models.PROTECT)
    payment_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses,on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name="fee_paid_user")
    discount = models.DecimalField(decimal_places=1,max_digits=100)
    pay_price = models.DecimalField(decimal_places=1,max_digits=100)
    paid_slip = models.FileField(upload_to="Fees_Documents")
    paid_slip_2 = models.FileField(upload_to="Fees_Documents")
    paid_approve_course_join = models.BooleanField(default=False)


    # def save(self, force_insert=False, force_update=False):
    #     if self.payment_id == "":
    #         payment_id_starts = "PAYMENT_ID :"
    #         fee_last_object = FeeDetails.objects.last()
    #         payment_id_last = fee_last_object.payment_id
    #         model_data = super(FeeDetails,self).save(force_insert,force_update)

    def __str__(self):
        return str(self.course.name)+" | "+str(self.user.first_name)

    # class Meta:
    #     ordering = "pk"

