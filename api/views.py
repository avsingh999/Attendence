from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import FacultysSerializer,StudentsSerializer
from home.models import Facultys,Students
# Create your views here.

class FacultysViewSet(ModelViewSet):
	queryset = Facultys.objects.all()
	serializer_class = FacultysSerializer

class StudentsViewSet(ModelViewSet):
	queryset = Students.objects.all()
	serializer_class = StudentsSerializer