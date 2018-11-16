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
# Create your views here.
 
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
                    # messages.add_message(request, messages.INFO, 'Logged in Successfully')
                    messages.success(request, 'Logged in Successfully')
                    response = HttpResponseRedirect(reverse('home:dashboard'))
                    response.set_cookie('name', "Shubham")
                    return response
                    # return HttpResponseRedirect('/dashboard', content)
        # render(request, 'home/faculty_dashboard.html', content)
                else:
                    content = {
                    'data': faculty_data
                    }
                    # messages.add_message(request, messages.ERROR, 'No match Wrong Password.')
                    messages.error(request, 'Sorry, either of your provided information is wrong.')
                    return render(request, 'home/home.html', content)
        except ObjectDoesNotExist:
            return render(request, 'home/home.html')
    else:
        return render(request, 'home/home.html')

def student_login(request):
    if request.method == 'POST':
        try:
            studnt_data = Students.objects.get(roll_no = request.POST['univ_rlno'])
            if studnt_data:
                if studnt_data.password == request.POST['name']:
                    request.session['student'] = studnt_data.pk
                    # content = {
                    #     'data': faculty_data
                    # }
                    messages.success(request, 'Logged in Successfully')
                    return HttpResponseRedirect(reverse('home:dashboard'))
        # render(request, 'home/faculty_dashboard.html', content)
                else:
                    messages.error(request, 'Sorry, either of your provided information is wrong.')
                    return HttpResponseRedirect(reverse('home:index'))
                    # return render(request, 'home/login.html', content)
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
        print("********* dashboard *********")
        for obj in sem1:
            print(obj.section)
        print("********* dashboard *********")


        semester_2_model = apps.get_model('home.Semester_2') 
        sem2 = semester_2_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem2:
            print(type((obj.professer_name)))

        semester_3_model = apps.get_model('home.Semester_3')
        sem3 = semester_3_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem3:
            print(obj.professer_name)

        semester_4_model = apps.get_model('home.Semester_4')
        sem4 = semester_4_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem4:
            print(obj.professer_name)

        semester_5_model = apps.get_model('home.Semester_5')
        sem5 = semester_5_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem5:
            print(obj.professer_name)

        semester_6_model = apps.get_model('home.Semester_6')
        sem6 = semester_6_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem6:
            print(obj.professer_name)

        semester_7_model = apps.get_model('home.Semester_7')
        sem7 = semester_7_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem7:
            print(obj.professer_name)

        semester_8_model = apps.get_model('home.Semester_8')
        sem8 = semester_8_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem8:
            print(obj.professer_name)

        semesters = [sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8]
        date = datetime.datetime.today().strftime('%Y-%m-%d')


        content = { 'data': faculty_data,'date':date, 'sem1':sem1, 'sem2':sem2, 'value': 10, 'sem3':sem3,'sem4':sem4,'sem5':sem5,'sem6':sem6,'sem7':sem7,'sem8':sem8,'sems':semesters}
        return render(request, 'dashboard/dashboard.html', content)

        # return render(request, 'home/view_students.html', content)




    elif 'student' in request.session:
        student_data = Students.objects.get(pk=request.session['student'])
        s = str("Semester_"+str(student_data.sem))
        student_subject = list()
        if(s == ("Semester_1")):
            print("***********************")
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_2")):
            print("***********************")
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_3")):
            print("***********************")
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_4")):
            print("***********************")
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_5")):
            print("***********************")
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_6")):
            print("***********************")
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_7")):
            print("***********************")
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_8")):
            print("***********************")
            student_subject = Semester_1.objects.all().filter(section=student_data.section)
            for i in student_subject:
                print(i.subject_code)

        section = Sections.objects.get(name=student_data.section)
        # attendance_data = daily_attendance.objects.filter(section = section.pk )
        content = {'student_data': student_data, 'data':student_data , 'student_subject':student_subject}
        return render(request, 'home/view_attendance_studnt.html', content)        # return HttpResponse(sectn_data)

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
    # return HttpResponseRedirect('/dashboard', content)
    return HttpResponseRedirect(reverse('home:dashboard'))

def logout(request):
    try:
        if 'faculty' in request.session:
            del request.session['faculty']
        elif 'student' in request.session:
            del request.session['student']
        # return HttpResponseRedirect(reverse('home:index', {
        #     'error_note': 'Logged out Successfully'
        # }))
        messages.success(request, "Logged Out Successfully")
        return HttpResponseRedirect(reverse('home:index'))

    except:
        messages.error(request, "Error in logging Out")
        return HttpResponseRedirect(reverse('home:index'))