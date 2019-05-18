from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
from datetime import date
# Create your models here.
class Sections(models.Model):
    name = models.CharField(max_length = 200, unique=True)
    creation_date = models.DateTimeField('date published', default=datetime.now)
    def __str__(self):
        return self.name

class UploadStudent(models.Model):
    image = models.FileField(upload_to='upload_location',)
class Facultys(models.Model):
    name = models.CharField(max_length = 200)
    username =  models.OneToOneField(User, on_delete=models.CASCADE)
    fileds = models.CharField(max_length=500, default='')
    qualification = models.CharField(max_length=201,default='')
    contact_no = models.CharField(max_length=25,default='')
    gender = models.IntegerField()

    def __str__(self):
        return self.username.username

class Semester_1(models.Model):
    subject_name = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    section = models.CharField(max_length=201)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    
class Students(models.Model):
    roll_no =  models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    phone = models.IntegerField(default = 1)
    gender = models.IntegerField()
    sem = models.IntegerField()
    section = models.CharField(max_length=201)
    slug = models.SlugField(max_length=251, default="1")

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Students, self).save(*args, **kwargs)
    def __str__(self):
        return self.roll_no.username

class Semester_2(models.Model):
    subject_name = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    section = models.CharField(max_length=201)

    def __str__(self):
        return self.subject_code

class Semester_3(models.Model):
    subject_name = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    section = models.CharField(max_length=201)
    def __str__(self):
        return self.subject_code

class Semester_4(models.Model):
    subject_name = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    section = models.CharField(max_length=201)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.subject_code
        
class Semester_5(models.Model):
    subject_name = models.CharField(max_length=201)
    section = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.subject_code
        
class Semester_6(models.Model):
    subject_name = models.CharField(max_length=201)
    section = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.subject_code
        
class Semester_7(models.Model):
    subject_name = models.CharField(max_length=201)
    section = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.subject_code
        
class Semester_8(models.Model):
    subject_name = models.CharField(max_length=201)
    section = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    # professer_name = models.OneToOneField(Facultys,on_delete=models.CASCADE, default=0)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.subject_code
        
class add_student_attendance(models.Model):
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    student_name = models.ForeignKey(Students, on_delete=models.CASCADE, default=0)
    semester = models.IntegerField()
    subject = models.CharField(max_length=201)
    batch = models.CharField(max_length=201)
    date = models.CharField(max_length=201)
    attend = models.IntegerField(default=0)