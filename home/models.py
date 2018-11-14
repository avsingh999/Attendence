from django.db import models
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
    username = models.CharField(max_length = 200, unique=True, default="aag001")
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 200)
    creation_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        # dat = self.name + self.email + self.section +" " +self.section
        return self.username

class Semester_1(models.Model):
    subject_name = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    section = models.CharField(max_length=201)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)

    # professer_name = models.OneToOneField(Facultys,on_delete=models.CASCADE, default=0)
 
class Students(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.CharField(max_length=200)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 200, default='student')

    phone = models.IntegerField(default = 1)
    mother_name = models.CharField(max_length=201)
    gender = models.IntegerField()
    sem = models.IntegerField()
    section = models.CharField(max_length=201)
    slug = models.SlugField(max_length=251, default="1")
    creation_date = models.DateTimeField('date published', default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Students, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Semester_2(models.Model):
    subject_name = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    section = models.CharField(max_length=201)

    # professer_name = models.OneToOneField(Facultys,on_delete=models.CASCADE, default='aag001')
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
    # professer_name = models.OneToOneField(Facultys,on_delete=models.CASCADE, default=0)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.subject_code
        
class Semester_6(models.Model):
    subject_name = models.CharField(max_length=201)
    section = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    # professer_name = models.OneToOneField(Facultys,on_delete=models.CASCADE, default=0)
    professer_name = models.ForeignKey(Facultys, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.subject_code
        
class Semester_7(models.Model):
    subject_name = models.CharField(max_length=201)
    section = models.CharField(max_length=201)
    subject_code = models.CharField(max_length=201)
    # professer_name = models.OneToOneField(Facultys,on_delete=models.CASCADE, default=0)
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