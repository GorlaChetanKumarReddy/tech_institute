from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from courses.check_and_return_functions import check_field_data_same

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
    complete_hours = models.DurationField(null=True,blank=True)
    end_timing = models.TimeField()
    duration_days = models.IntegerField()
    Discription1 = models.TextField()
    Discription2 = models.TextField(null=True,blank=True)
    Discription3 = models.TextField(null=True,blank=True)
    CourseFile = models.FileField(upload_to="CourseFile")
    CourseFile2 = models.FileField(upload_to="CourseFile",null=True,blank=True)
    is_active = models.BooleanField(default=False)
    title_1 = models.CharField(max_length=200,null=True,blank=True,verbose_name="TITLE 1")
    title_1_data = models.TextField(null=True,blank=True,verbose_name="TITLE 1 DATA")
    title_2 = models.CharField(max_length=200,null=True,blank=True,verbose_name="TITLE ")
    title_2_data = models.TextField(blank=True,null=True,verbose_name="TITLE 2 DATA")
    title_3 = models.CharField(max_length=200,null=True,blank=True,verbose_name="TITLE 3")
    title_3_data = models.TextField(blank=True,null=True,verbose_name="TITLE 3 DATA")
    title_4 = models.CharField(max_length=200,null=True,blank=True,verbose_name="TITLE 4")
    title_4_data = models.TextField(blank=True,null=True,verbose_name="TITLE 4 DATA")

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):


        fields_li = ['name', 'price', 'category_id', 'image1',
                     'faculty_name','start_date', 'end_date',
                     'start_timing','complete_hours','end_timing','duration_days',
                     'Discription1','Discription2',
                     'Discription3','CourseFile','CourseFile2','is_active',
                     'title_1','title_1_data',
                     'title_2','title_2_data',
                     'title_3','title_3_data',
                     'title_4','title_4_data']

        values_li = [
                self.name,self.price,self.category_id,self.image1,self.faculty_name,
                self.start_date,self.end_date,self.start_timing,self.complete_hours,self.end_timing,
                self.duration_days,self.Discription1,self.Discription2,self.Discription3,self.CourseFile,
                self.CourseFile2,self.is_active,self.title_1,self.title_1_data,self.title_2,self.title_2_data,
                self.title_3,self.title_3_data,self.title_4,self.title_4_data
                ]

        try:
            coobj = Courses.objects.filter(id=self.id).last()
            save_ob = Updated_Courses()
            save_ob.added_by = self.added_by
            save_ob.course = coobj
            save_ob.save()

            check_field_data_same(
                check_obj=coobj,
                save_obj=save_ob,
                fieldnames=fields_li,
                values=values_li
            )
        except Exception as e:
            print(str(e))
            UpObj = Updated_Courses()
            UpObj.added_by = self.added_by
            UpObj.course_id = self.id
            UpObj.name = self.name
            UpObj.price = self.price
            UpObj.category = self.category
            UpObj.image1 = self.image1
            UpObj.faculty_name = self.faculty_name
            UpObj.start_date = self.start_date
            UpObj.end_date = self.end_date
            UpObj.start_timing = self.start_timing
            UpObj.complete_hours = self.complete_hours
            UpObj.end_timing = self.end_timing
            UpObj.duration_days = self.duration_days
            UpObj.Discription1 = self.Discription1
            UpObj.Discription2 = self.Discription2
            UpObj.Discription3 = self.Discription3
            UpObj.CourseFile = self.CourseFile
            UpObj.CourseFile2 = self.CourseFile2
            UpObj.is_active = self.is_active
            UpObj.title_1 = self.title_1
            UpObj.title_1_data = self.title_1_data
            UpObj.title_2 = self.title_2
            UpObj.title_2_data = self.title_2_data
            UpObj.title_3 = self.title_3
            UpObj.title_3_data = self.title_3_data
            UpObj.title_4 = self.title_4
            UpObj.title_4_data = self.title_4_data
            UpObj.save()
        super(Courses, self).save(force_insert, force_update)


class Updated_Courses(MandetoryFields):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True, blank=True)
    price = models.BigIntegerField(default=0)
    category = models.ForeignKey(CoursesCategory, on_delete=models.PROTECT,null=True, blank=True)
    image1 = models.ImageField(upload_to="updated/courses_images",null=True, blank=True)
    faculty_name = models.CharField(max_length=150,null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_timing = models.TimeField(null=True, blank=True)
    complete_hours = models.DurationField(null=True, blank=True)
    end_timing = models.TimeField(null=True, blank=True)
    duration_days = models.IntegerField(null=True, blank=True)
    Discription1 = models.TextField(null=True, blank=True)
    Discription2 = models.TextField(null=True, blank=True)
    Discription3 = models.TextField(null=True, blank=True)
    CourseFile = models.FileField(upload_to="CourseFile",null=True, blank=True)
    CourseFile2 = models.FileField(upload_to="CourseFile", null=True, blank=True)
    is_active = models.BooleanField(default=False)
    title_1 = models.CharField(max_length=200, null=True, blank=True, verbose_name="TITLE 1")
    title_1_data = models.TextField(null=True, blank=True, verbose_name="TITLE 1 DATA")
    title_2 = models.CharField(max_length=200, null=True, blank=True, verbose_name="TITLE ")
    title_2_data = models.TextField(blank=True, null=True, verbose_name="TITLE 2 DATA")
    title_3 = models.CharField(max_length=200, null=True, blank=True, verbose_name="TITLE 3")
    title_3_data = models.TextField(blank=True, null=True, verbose_name="TITLE 3 DATA")
    title_4 = models.CharField(max_length=200, null=True, blank=True, verbose_name="TITLE 4")
    title_4_data = models.TextField(blank=True, null=True, verbose_name="TITLE 4 DATA")

    def __str__(self):
        return str(self.course.name)


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

