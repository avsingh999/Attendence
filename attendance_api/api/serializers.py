from .models import Facultys,Students,add_student_attendance,Semester_2,Semester_1,Semester_3,Semester_4,Semester_5,Semester_6,Semester_7,Semester_8
from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate, login

class FacultysSerializer(serializers.ModelSerializer):
	class Meta:
		model = Facultys
		exclude = []

class StudentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Students
		exclude = []

class AttendancesSerializer(serializers.ModelSerializer):
	class Meta:
		model = add_student_attendance
		exclude = []

class Semester1Serializer(serializers.ModelSerializer):
	class Meta:
		model = Semester_1
		exclude = []

class Semester2Serializer(serializers.ModelSerializer):
	class Meta:
		model = Semester_2
		exclude = []

class Semester3Serializer(serializers.ModelSerializer):
	class Meta:
		model = Semester_3
		exclude = []

class Semester4Serializer(serializers.ModelSerializer):
	class Meta:
		model = Semester_4
		exclude = []

class Semester5Serializer(serializers.ModelSerializer):
	class Meta:
		model = Semester_5
		exclude = []

class Semester6Serializer(serializers.ModelSerializer):
	class Meta:
		model = Semester_6
		exclude = []

class Semester7Serializer(serializers.ModelSerializer):
	class Meta:
		model = Semester_7
		exclude = []

class Semester8Serializer(serializers.ModelSerializer):
	class Meta:
		model = Semester_8
		exclude = []

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()
	def validate(self, data):
		username = data.get('username', "")
		password = data.get("password", "")
		if username and password:
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					data["user"] = user
				else:
					msg = "deactivate"
					raise exceptions.ValidationError(msg)
			else:
				msg = "wrong credentials"
				raise exceptions.ValidationError(msg)
		else:
			msg = "Required fields please fill"
			raise exceptions.ValidationError(msg)
		return data

class AddAttendanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = add_student_attendance
		exclude = []

	