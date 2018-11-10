from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from home.models import *
#from .models import *
from home.models import *
from django.contrib import messages
from home.templatetags import *
# Create your views here.
from django.apps import apps
import datetime
 

def todays_add_attendance(request,prof,semester,sub,date):
    total_students = request.POST['total_studnt']
    present_students = request.POST.getlist('present[]')
    Facultys_model = apps.get_model('home.Facultys')
    proffeser = Facultys_model.objects.all().filter(username=prof)

    Students_list_model = apps.get_model('home.Students')
    students_list = Students_list_model.objects.all().filter(sem=semester)
    print("************************* ")
    print(proffeser[0])
    for i in students_list:
        Students_model = apps.get_model('home.Students')
        add_student_attendance_model = apps.get_model('home.add_student_attendance')
        add__attendance_model = add_student_attendance_model()
        add__attendance_model.professer_name = proffeser[0]
        add__attendance_model.student_name = i
        add__attendance_model.semester = semester
        add__attendance_model.subject = sub
        add__attendance_model.batch = 'cs'
        add__attendance_model.date = date
        if i.roll_no in present_students:
            add__attendance_model.attend = 1
        else:
            add__attendance_model.attend = 0
        add__attendance_model.save()      
    # print(request.POST.getlist('present[]'))
    # print(prof,semester,sub,date)
    messages.success(request, 'Attendance Added Successfully.')
    reder = '/add_attendance/sem'+str(semester)+'/'+sub
    return HttpResponseRedirect(reder)

def add_attendance(request):
    # return HttpResponse("shubahm")
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)
    sectn_data = Sections.objects.get(name=faculty_data.section)
    print("****** section_data ********")
    print(sectn_data)

    semester_1_model = apps.get_model('home.Semester_1')
    sem1 = semester_1_model.objects.all().filter(professer_name=faculty_data)
    for obj in sem1:
        print(obj)
        

    semester_2_model = apps.get_model('home.Semester_2') 
    sem2 = semester_2_model.objects.all().filter(professer_name=faculty_data)
    for obj in sem2:
        print(type((obj.professer_name)))
        if(str(obj.professer_name) == 'aag001'):
            print("****** aa gya ****")
    
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

    
    content = { 'data': faculty_data, 'sem1':sem1, 'sem2':sem2, 'value': 10, 'sem3':sem3,'sem4':sem4,'sem5':sem5,'sem6':sem6,'sem7':sem7,'sem8':sem8}
    return render(request, 'dashboard/add_attendance.html', content)
    
def add_attendance_sem_1(request,id):

    student_model = apps.get_model('home.Students')
    students = student_model.objects.all().filter(sem=1)
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    print("***************sem 1 student*************")
    print(faculty_data.username)
    for i in students:
        print(i)
    return render(request, 'dashboard/add_stud_attendance.html', {'students':students, 'sub':id, "semester":1,'date':date, 'proff':faculty_data.username})


    # return HttpResponse("IIII 1")
def add_attendance_sem_2(request,id):
    student_model = apps.get_model('home.Students')
    students = student_model.objects.all().filter(sem=2) 
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    print("***************sem 1 student*************")
    print(faculty_data.username)
    for i in students:
        print(i)
    return render(request, 'dashboard/add_stud_attendance.html', {'students':students, 'sub':id, "semester":2,'date':date, 'proff':faculty_data.username})

def add_attendance_sem_3(request,id):
    student_model = apps.get_model('home.Students')
    students = student_model.objects.all().filter(sem=3) 
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    print("***************sem 1 student*************")
    print(faculty_data.username)
    for i in students:
        print(i)
    return render(request, 'dashboard/add_stud_attendance.html', {'students':students, 'sub':id, "semester":3,'date':date, 'proff':faculty_data.username})

def add_attendance_sem_4(request,id):
    student_model = apps.get_model('home.Students')
    students = student_model.objects.all().filter(sem=4) 
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    print("***************sem 1 student*************")
    print(faculty_data.username)
    for i in students:
        print(i)
    return render(request, 'dashboard/add_stud_attendance.html', {'students':students, 'sub':id, "semester":4,'date':date, 'proff':faculty_data.username})

def add_attendance_sem_5(request,id):
    student_model = apps.get_model('home.Students')
    students = student_model.objects.all().filter(sem=5) 
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    print("***************sem 1 student*************")
    print(faculty_data.username)
    for i in students:
        print(i)
    return render(request, 'dashboard/add_stud_attendance.html', {'students':students, 'sub':id, "semester":5,'date':date, 'proff':faculty_data.username})

def add_attendance_sem_6(request,id):
    student_model = apps.get_model('home.Students')
    students = student_model.objects.all().filter(sem=6) 
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    print("***************sem 1 student*************")
    print(faculty_data.username)
    for i in students:
        print(i)
    return render(request, 'dashboard/add_stud_attendance.html', {'students':students, 'sub':id, "semester":6,'date':date, 'proff':faculty_data.username})

def add_attendance_sem_7(request,id):
    student_model = apps.get_model('home.Students')
    students = student_model.objects.all().filter(sem=7) 
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    print("***************sem 1 student*************")
    print(faculty_data.username)
    for i in students:
        print(i)
    return render(request, 'dashboard/add_stud_attendance.html', {'students':students, 'sub':id, "semester":7,'date':date, 'proff':faculty_data.username})

def add_attendance_sem_8(request,id):
    student_model = apps.get_model('home.Students')
    students = student_model.objects.all().filter(sem=8) 
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    print("***************sem 1 student*************")
    print(faculty_data.username)
    for i in students:
        print(i)
    return render(request, 'dashboard/add_stud_attendance.html', {'students':students, 'sub':id, "semester":8,'date':date, 'proff':faculty_data.username})

def today_attendance(request):
    if request.method == 'POST':
        total_students = request.POST['total_studnt']
        student = ','.join(request.POST.getlist('present[]'))
        faculty_data = Facultys.objects.get(pk=request.session['faculty'])
        sectn_data = Sections.objects.get(name=faculty_data.section)
        add_attendance = sectn_data.daily_attendance_set.create(student=student, section=request.POST['section'], faculty=request.session['faculty'])
        add_attendance.save()
        # for student in request.POST.getlist('present[]'):
            # add_attendance = daily_attendance(student = student, section = request.POST['section'], faculty= request.session['faculty'])
            # check = add_attendance.save()
            # content_data = { student : student }
            # content.append(content_data)
        # if check:
        messages.success(request, 'Attendance Added Successfully.')
    return render(request, 'dashboard/add_attendance.html')

def view_attendance(request):
    if 'faculty' in request.session:
        sessn_val = request.session['faculty']
        faculty_data = Facultys.objects.get(pk=sessn_val)
        sectn_data = Sections.objects.get(name=faculty_data.section)
        print("****** section_data ********")
        print(sectn_data)

        semester_1_model = apps.get_model('home.Semester_1')
        sem1 = semester_1_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem1:
            print(obj)
            

        semester_2_model = apps.get_model('home.Semester_2') 
        sem2 = semester_2_model.objects.all().filter(professer_name=faculty_data)
        for obj in sem2:
            print(type((obj.professer_name)))
            if(str(obj.professer_name) == 'aag001'):
                print("****** aa gya ****")
        
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

        
        content = { 'data': faculty_data, 'sem1':sem1, 'sem2':sem2, 'value': 10, 'sem3':sem3,'sem4':sem4,'sem5':sem5,'sem6':sem6,'sem7':sem7,'sem8':sem8}
        # return render(request, 'dashboard/view_attendance_semadd_attendance.html', content)

        return render(request, 'home/view_attendance.html', content)
    elif 'student' in request.session:
        student_data = Students.objects.get(pk=request.session['student'])
        s = str("Semester_"+str(student_data.sem))
        student_subject = list()
        if(s == ("Semester_1")):
            print("***********************")
            student_subject = Semester_1.objects.all()
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_2")):
            print("***********************")
            student_subject = Semester_1.objects.all()
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_3")):
            print("***********************")
            student_subject = Semester_1.objects.all()
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_4")):
            print("***********************")
            student_subject = Semester_1.objects.all()
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_5")):
            print("***********************")
            student_subject = Semester_1.objects.all()
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_6")):
            print("***********************")
            student_subject = Semester_1.objects.all()
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_7")):
            print("***********************")
            student_subject = Semester_1.objects.all()
            for i in student_subject:
                print(i.subject_code)
        elif(s == ("Semester_8")):
            print("***********************")
            student_subject = Semester_1.objects.all()
            for i in student_subject:
                print(i.subject_code)

        section = Sections.objects.get(name=student_data.section)
        # attendance_data = daily_attendance.objects.filter(section = section.pk )
        content = {'student_data': student_data, 'data':student_data , 'student_subject':student_subject}
    return render(request, 'home/view_attendance_studnt.html', content)
    # return render(request, 'dashboard/add_attendance.html')
def view_attendance_sem(request,sem,sub):
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)

    add_student_attendance_model = apps.get_model('home.add_student_attendance')
    attendance_of_student = add_student_attendance_model.objects.all().filter(semester=sem,subject=sub)

    print("****** come ***************")

    return HttpResponse('hello')

def view_my_attendance_sem(request,roll,sub):
    student_data = Students.objects.get(pk=request.session['student'])
    add_student_attendance_model = apps.get_model('home.add_student_attendance')
    attendance_of_student = add_student_attendance_model.objects.all().filter(student_name=student_data,subject=sub)
    return HttpResponse('hello')


def day_attendance(request, attendance_date):
    # return HttpResponse(attendance_date)
    if 'faculty' in request.session:
        faculty_data = Facultys.objects.get(pk = request.session['faculty'])
        section = Sections.objects.get(name=faculty_data.section)
        attendance_data = daily_attendance.objects.filter(faculty = faculty_data.pk, attendance_date = attendance_date )
        content = {  'data': faculty_data, 'attendance_data' : attendance_data, 'section_data': section }
        return render(request, 'attendance/day_attendance.html', content)
    # elif 'student' in request.session:
    #     student_data = Students.objects.get(pk=request.session['student'])
    #     section = Sections.objects.get(name=student_data.section)
    #     attendance_data = daily_attendance.objects.filter(section = section.pk )
    #     content = { 'attendance_data' : attendance_data }
    return render(request, 'attendance/day_attendance.html', content)

def student_profile(request, slug):
    # return HttpResponse(slug)
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)
    sectn_data = Sections.objects.get(name=faculty_data.section)
    studnt_data = Students.objects.get(slug=slug)
    attendance_data = daily_attendance.objects.filter(faculty=faculty_data.pk, section_id = sectn_data.pk)
    content = {'data': faculty_data, 'studnt_data':studnt_data, 'sectn_data': sectn_data, 'attendance_data':attendance_data}
    return render(request, 'attendance/student_profile.html', content)

def view_messages(request):
    if 'student' in request.session:
        student_data = Students.objects.get(pk=request.session['student'])
        section = Sections.objects.get(pk=student_data.section_id)
        faculty = Facultys.objects.get(section_id = section.pk)
        if request.method == 'POST':
            data = allmessages(message_text = request.POST['msg_txt'], m_from = request.session['student'], m_to = faculty.pk)
            check=data.save()
            messages.success(request, "Message sent Successfully.")
        messages_all = allmessages.objects.filter(m_to = request.session['student'], m_from = faculty.pk )
        content = { 'messages_all':messages_all, 'data':student_data }
        # return HttpResponse(request.POST['editor1'])
    elif 'faculty' in request.session:
        faculty = Facultys.objects.get(pk=request.session['faculty'])
        section = Sections.objects.get(pk=faculty.section_id)
        if request.method == 'POST':
            students = ','.join(request.POST.getlist('send_message[]'))
            data = allmessages(message_text=request.POST['msg_txt'], m_from=request.session['faculty'], m_to=students)
            check = data.save()
            messages.success(request, "Message sent Successfully.")
        messages_all = allmessages.objects.filter(m_from=request.session['faculty'])
        content = { 'messages_all':messages_all, 'data':faculty }
    return render(request, 'attendance/view_messages.html', content)

def recieved_messages(request):
    if 'faculty' in request.session:
        faculty = Facultys.objects.get(pk=request.session['faculty'])
        section = Sections.objects.get(pk=faculty.section_id)
        messages_all = allmessages.objects.filter(m_to=request.session['faculty'])
        content = {'messages_all': messages_all, 'data': faculty}
    return render(request, 'attendance/recieved_messages.html', content)

def new_faculty_message(request):
    if 'faculty' in request.session:
        faculty = Facultys.objects.get(pk=request.session['faculty'])
        section = Sections.objects.get(pk=faculty.section_id)
        student_data = Students.objects.filter(section_id = section.pk)
        # messages_all = allmessages.objects.filter(m_to=request.session['faculty'])
        content = {'data': faculty, 'student_data': student_data}
    return render(request, 'attendance/new_faculty_message.html', content)
