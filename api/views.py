from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import FacultysSerializer,StudentsSerializer,AttendancesSerializer
from home.models import Facultys,Students,add_student_attendance
# Create your views here.

class FacultysViewSet(ModelViewSet):
	queryset = Facultys.objects.all()
	serializer_class = FacultysSerializer

class StudentsViewSet(ModelViewSet):
	queryset = Students.objects.all()
	serializer_class = StudentsSerializer

class AttendancesViewSet(ModelViewSet):
	queryset = add_student_attendance.objects.all()
	serializer_class = AttendancesSerializer