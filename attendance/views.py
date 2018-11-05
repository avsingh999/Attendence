from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from home.models import *
#from .models import *
from home.models import *
from django.contrib import messages
from home.templatetags import *
# Create your views here.
from django.apps import apps

def add_attendance(request):
    # return HttpResponse("shubahm")
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)
    sectn_data = Sections.objects.get(name=faculty_data.section)
    print("****** section_data ********")
    print(faculty_data.section)

    semester_1_model = apps.get_model('home.Semester_1')
    sem1 = semester_1_model.objects.all()

    for obj in sem1:
        print(obj.professer_name)
        if(obj.professer_name == 'aag001'):
            print("****** aa gya ****")

    semester_2_model = apps.get_model('home.Semester_2')
    sem2 = semester_2_model.objects.all()
    for obj in sem2:
        print(type(str(obj.professer_name)))
        if(str(obj.professer_name) == 'aag001'):
            print("****** aa gya ****")
    
    semester_3_model = apps.get_model('home.Semester_3')
    sem3 = semester_3_model.objects.all()
    for obj in sem3:
        print(obj.professer_name)

    semester_4_model = apps.get_model('home.Semester_4')
    sem4 = semester_4_model.objects.all()
    for obj in sem4:
        print(obj.professer_name)

    semester_5_model = apps.get_model('home.Semester_5')
    sem5 = semester_5_model.objects.all()
    for obj in sem5:
        print(obj.professer_name)

    semester_6_model = apps.get_model('home.Semester_6')
    sem6 = semester_6_model.objects.all()
    for obj in sem6:
        print(obj.professer_name)

    semester_7_model = apps.get_model('home.Semester_7')
    sem7 = semester_7_model.objects.all()
    for obj in sem7:
        print(obj.professer_name)

    semester_8_model = apps.get_model('home.Semester_8')
    sem8 = semester_8_model.objects.all()
    for obj in sem8:
        print(obj.professer_name)
    content = { 'data': faculty_data, 'sem1':sem1, 'sem2':sem2, 'sem3':sem3,'sem4':sem4,'sem5':sem5,'sem6':sem6,'sem7':sem7,'sem8':sem8}
    return render(request, 'dashboard/add_attendance.html', content)
    
def add_attendance_sem(request):
    return HttpResponse("IIII")

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
        faculty_data = Facultys.objects.get(pk = request.session['faculty'])
        section = Sections.objects.get(name=faculty_data.section)
        attendance_data = daily_attendance.objects.filter(faculty = faculty_data.pk, section = section.pk )
        content = {  'data': faculty_data, 'attendance_data' : attendance_data, 'section_data': section }
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
        attendance_data = daily_attendance.objects.filter(section = section.pk )
        content = { 'attendance_data' : attendance_data, 'student_data': student_data, 'data':student_data , 'student_subject':student_subject}
    return render(request, 'home/view_attendance_studnt.html', content)
    # return render(request, 'dashboard/add_attendance.html')

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
