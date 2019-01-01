from home.models import Facultys,Students,add_student_attendance
from rest_framework import serializers

class FacultysSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Facultys
		exclude = []


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Students
		exclude = []

class AttendancesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = add_student_attendance
		exclude = []