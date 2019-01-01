from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.contrib import messages
from django.apps import apps
from django.views import generic
import datetime
from django.core.serializers.json import DjangoJSONEncoder
 
def index(request):
    if request.method == 'POST':
        try:
            faculty_data = Facultys.objects.get(email = request.POST['email'])
            if faculty_data:
                if faculty_data.password == request.POST['password']:
                    request.session['faculty'] = faculty_data.pk
                    content = {
                        'data': faculty_data
                    }
                    messages.success(request, 'Logged in Successfully')
                    response = HttpResponseRedirect(reverse('home:dashboard'))
                    response.set_cookie('name', "Shubham")
                    return response
                else:
                    content = {
                    'data': faculty_data
                    }
                    messages.error(request, 'Sorry, either of your provided information is wrong.')
                    return render(request, 'home/home.html', content)
        except ObjectDoesNotExist:
            return render(request, 'home/home.html')
    else:
        return render(request, 'home/home.html')

def student_login(request):
    if request.method == 'POST':
        try:
            studnt_data = Students.objects.get(roll_no = request.POST.get('univ_rlno'))
            if studnt_data:
                if studnt_data.password == request.POST['name']:
                    request.session['student'] = studnt_data.pk
                    messages.success(request, 'Logged in Successfully')
                    return HttpResponseRedirect(reverse('home:dashboard'))
                else:
                    messages.error(request, 'Sorry, either of your provided information is wrong.')
                    return HttpResponseRedirect(reverse('home:index'))
        except ObjectDoesNotExist:
            messages.error(request, 'User does not exist.')
            return HttpResponseRedirect(reverse('home:index'))
    else:
        return render(request, 'home/login.html')
 
def dashboard_faculty(request):
    if 'faculty' in request.session:
        sessn_val = request.session['faculty']
        faculty_data = Facultys.objects.get(pk=sessn_val)
        student_data = Students.objects.all().filter(sem=1)
        content = {'data': faculty_data, 'sectn_data': student_data}

        semester_1_model = apps.get_model('home.Semester_1')
        sem1 = semester_1_model.objects.all().filter(professer_name=faculty_data)


        semester_2_model = apps.get_model('home.Semester_2') 
        sem2 = semester_2_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem2:
            pass
        semester_3_model = apps.get_model('home.Semester_3')
        sem3 = semester_3_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem3:
            pass
        semester_4_model = apps.get_model('home.Semester_4')
        sem4 = semester_4_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem4:
            pass
        semester_5_model = apps.get_model('home.Semester_5')
        sem5 = semester_5_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem5:
            pass
        semester_6_model = apps.get_model('home.Semester_6')
        sem6 = semester_6_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem6:
            pass
        semester_7_model = apps.get_model('home.Semester_7')
        sem7 = semester_7_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem7:
            pass
        semester_8_model = apps.get_model('home.Semester_8')
        sem8 = semester_8_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem8:
            pass
        semesters = [sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8]
        date = datetime.datetime.today().strftime('%Y-%m-%d')


        content = { 'data': faculty_data,'date':date, 'sem1':sem1, 'sem2':sem2, 'value': 10, 'sem3':sem3,'sem4':sem4,'sem5':sem5,'sem6':sem6,'sem7':sem7,'sem8':sem8,'sems':semesters}
        return render(request, 'dashboard/dashboard.html', content)


    elif 'student' in request.session:
        student_data = Students.objects.get(pk=request.session['student'])
        s = str("Semester_"+str(student_data.sem))
        student_subject = list()
        if(s == ("Semester_1")):
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
        elif(s == ("Semester_2")):
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
        elif(s == ("Semester_3")):
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
        elif(s == ("Semester_4")):
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
        elif(s == ("Semester_5")):
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
        elif(s == ("Semester_6")):
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
        elif(s == ("Semester_7")):
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
        elif(s == ("Semester_8")):
            student_subject = Semester_1.objects.all().filter(section=student_data.section)

        section = Sections.objects.get(name=student_data.section)
        content = {'student_data': student_data, 'data':student_data , 'student_subject':student_subject}
        return render(request, 'home/view_attendance_studnt.html', content)   

def add_student(request):
    content={}
    if request.method == 'POST':
        faculty_data = Facultys.objects.get(pk=request.POST['id_faculty'])
        sectn_data = Sections.objects.get(name=faculty_data.section)
        stdnt = sectn_data.students_set.create(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone_no'], gender=request.POST['gender'], mother_name=request.POST['mother_name'])
        chek = stdnt.save()
        today = datetime.datetime.now()
        get_lastid = Students.objects.latest('id')
        set_roll_no = sectn_data.name + str(today.year) + str(get_lastid.id)
        student_data = Students.objects.get(id=get_lastid.id)
        student_data.roll_no = set_roll_no
        check1 = student_data.save()
        if get_lastid:
            messages.success(request, "Student Added Successfully")
        else:
            messages.error(request, "Error in adding student")
    return HttpResponseRedirect(reverse('home:dashboard'))

def logout(request):
    try:
        if 'faculty' in request.session:
            del request.session['faculty']
        elif 'student' in request.session:
            del request.session['student']
        messages.success(request, "Logged Out Successfully")
        return HttpResponseRedirect(reverse('home:index'))

    except:
        messages.error(request, "Error in logging Out")
        return HttpResponseRedirect(reverse('home:index'))