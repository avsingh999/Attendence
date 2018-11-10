"""attendance_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'attendance'
urlpatterns = [
    url(r'^student_profile/(?P<slug>.*)/$', views.student_profile, name="student_profile"),
    url(r'^add_attendance/$', views.add_attendance, name="add_attendance"),
     path('add_attendance/sem1/<str:id>', views.add_attendance_sem_1, name = "add_attendance_sem_1"),
     path('add_attendance/sem2/<str:id>', views.add_attendance_sem_2, name = "add_attendance_sem_2"),
     path('add_attendance/sem3/<str:id>', views.add_attendance_sem_3, name = "add_attendance_sem_3"),
     path('add_attendance/sem4/<str:id>', views.add_attendance_sem_4, name = "add_attendance_sem_4"),
     path('add_attendance/sem5/<str:id>', views.add_attendance_sem_5, name = "add_attendance_sem_5"),
     path('add_attendance/sem6/<str:id>', views.add_attendance_sem_6, name = "add_attendance_sem_6"),
     path('add_attendance/sem7/<str:id>', views.add_attendance_sem_7, name = "add_attendance_sem_7"),
     path('add_attendance/sem8/<str:id>', views.add_attendance_sem_8, name = "add_attendance_sem_8"),
    # url(r'^add_attendance/', views.add_attendance_sem, name="add_attendance_sem"),
    url(r'^today_attendance/$', views.today_attendance, name="today_attendance"),
    path('todays_add_attendance/<str:prof>/<int:semester>/<str:sub>/<str:date>', views.todays_add_attendance, name="todays_add_attendance"),
    url(r'^view_attendance/$', views.view_attendance, name="view_attendance"),
    path('view_attendance_sem/<int:sem>/<str:sub>', views.view_attendance_sem, name="view_attendance_sem"),
    path('view_my_attendance_sem/<int:roll>/<str:sub>', views.view_my_attendance_sem, name="view_my_attendance_sem"),

    url(r'^day_attendance/(?P<attendance_date>.*)/$', views.day_attendance, name="day_attendance"),
    url(r'^view_messages/$', views.view_messages, name="view_messages"),
    url(r'^new_message/$', views.new_faculty_message, name="new_faculty_message"),
    url(r'^recieved_messages/$', views.recieved_messages, name="recieved_messages"),
    # url(r'^login_check/$', views.login_check, name="login_check"),
]
