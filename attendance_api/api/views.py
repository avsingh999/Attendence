from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import LoginSerializer,AddAttendanceSerializer,FacultysSerializer,StudentsSerializer,AttendancesSerializer,Semester2Serializer,Semester1Serializer,Semester3Serializer,Semester4Serializer,Semester5Serializer,Semester6Serializer,Semester7Serializer,Semester8Serializer
from .models import Facultys,Students,add_student_attendance,Semester_2,Semester_1,Semester_3,Semester_4,Semester_5,Semester_6,Semester_7,Semester_8
from django.contrib.auth import login
from rest_framework.authtoken.models import Token

# Create your views here.
class DashBoardViewSet(ViewSet):
	def list(self, request):
		if(request.user.groups.all()[0].name=="Facultys"):
			queryset = Facultys.objects.filter(username=request.user)			
			user = get_object_or_404(queryset, username=request.user)
			serializer = FacultysSerializer(user)
			queryset_1 = Semester_1.objects.all().filter(professer_name=user)
			serializer_class_1 = Semester1Serializer(queryset_1, many=True,context={'request': request})
			queryset_2 = Semester_2.objects.all().filter(professer_name=user)
			serializer_class_2 = Semester2Serializer(queryset_2, many=True,context={'request': request})
			queryset_3 = Semester_3.objects.all().filter(professer_name=user)
			serializer_class_3 = Semester3Serializer(queryset_3, many=True,context={'request': request})
			queryset_4 = Semester_4.objects.all().filter(professer_name=user)
			serializer_class_4 = Semester4Serializer(queryset_4, many=True,context={'request': request})
			queryset_5 = Semester_5.objects.all().filter(professer_name=user)
			serializer_class_5 = Semester5Serializer(queryset_5, many=True,context={'request': request})
			queryset_6 = Semester_6.objects.all().filter(professer_name=user)
			serializer_class_6 = Semester6Serializer(queryset_6, many=True,context={'request': request})
			queryset_7 = Semester_7.objects.all().filter(professer_name=user)
			serializer_class_7 = Semester7Serializer(queryset_7, many=True,context={'request': request})
			queryset_8 = Semester_8.objects.all().filter(professer_name=user)
			serializer_class_8 = Semester8Serializer(queryset_8, many=True,context={'request': request})	
			
			return Response([serializer.data,serializer_class_1.data,serializer_class_2.data,serializer_class_2.data,serializer_class_3.data,serializer_class_4.data,serializer_class_5.data,serializer_class_6.data,serializer_class_7.data,serializer_class_8.data])
		else:	
			user = Students.objects.filter(roll_no=request.user)
			serializer = StudentsSerializer(user[0])			
			if(user[0].sem==1):
				queryset = Semester_1.objects.all()
				serializer_class = Semester1Serializer(queryset, many=True,context={'request': request})
			elif(user[0].sem==2):
				queryset = Semester_2.objects.all()
				serializer_class = Semester2Serializer(queryset, many=True,context={'request': request})
			elif(user[0].sem==3):
				queryset = Semester_3.objects.all()
				serializer_class = Semester3Serializer(queryset, many=True,context={'request': request})
			elif(user[0].sem==4):
				queryset = Semester_4.objects.all()
				serializer_class = Semester4Serializer(queryset, many=True,context={'request': request})
			elif(user[0].sem==5):
				queryset = Semester_5.objects.all()
				serializer_class = Semester5Serializer(queryset, many=True,context={'request': request})
			elif(user[0].sem==6):
				queryset = Semester_6.objects.all()
				serializer_class = Semester6Serializer(queryset, many=True,context={'request': request})
			elif(user[0].sem==7):
				queryset = Semester_7.objects.all()
				serializer_class = Semester7Serializer(queryset, many=True,context={'request': request})
			elif(user[0].sem==8):
				queryset = Semester_8.objects.all()
				serializer_class = Semester8Serializer(queryset, many=True,context={'request': request})
			serializer_list = [serializer.data,serializer_class.data]
			return Response(serializer_list)

class FacultysViewSet(ViewSet):
	def list(self, request):
		queryset = Facultys.objects.all()
		serializer_class = FacultysSerializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)
	def retrieve(self, request, pk=None):
		queryset = Facultys.objects.all()
		user = get_object_or_404(queryset, pk=pk)
		serializer = FacultysSerializer(user)
		return Response(serializer.data)

class StudentsViewSet(ViewSet):
	def list(self, request):
		queryset = Students.objects.all()
		serializer_class = StudentsSerializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)
	def retrieve(self, request, pk=None):
		queryset = Students.objects.all()
		user = get_object_or_404(queryset, pk=pk)
		serializer = StudentsSerializer(user)
		return Response(serializer.data)

class AttendancesViewSet(ViewSet):
	def list(self, request):
		queryset = add_student_attendance.objects.all()
		serializer_class = AttendancesSerializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)

class Semester1viewSet(ViewSet):
	def list(self, request):
		queryset = Semester_1.objects.all()
		serializer_class = Semester1Serializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)

	def retrieve(self, request, pk=None):
		queryset = Semester_1.objects.all()
		sem = get_object_or_404(queryset, pk=pk)
		serializer = Semester1Serializer(sem)
		return Response(serializer.data)

class Semester2viewSet(ViewSet):
	def list(self, request):
		queryset = Semester_2.objects.all()
		serializer_class = Semester2Serializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)

	def retrieve(self, request, pk=None):
		queryset = Semester_2.objects.all()
		sem = get_object_or_404(queryset, pk=pk)
		serializer = Semester2Serializer(sem)
		return Response(serializer.data)

class Semester3viewSet(ViewSet):
	def list(self, request):
		queryset = Semester_3.objects.all()
		serializer_class = Semester3Serializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)

	def retrieve(self, request, pk=None):
		queryset = Semester_3.objects.all()
		sem = get_object_or_404(queryset, pk=pk)
		serializer = Semester3Serializer(sem)
		return Response(serializer.data)

class Semester4viewSet(ViewSet):
	def list(self, request):
		queryset = Semester_4.objects.all()
		serializer_class = Semester4Serializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)

	def retrieve(self, request, pk=None):
		queryset = Semester_4.objects.all()
		sem = get_object_or_404(queryset, pk=pk)
		serializer = Semester4Serializer(sem)
		return Response(serializer.data)

class Semester5viewSet(ViewSet):
	def list(self, request):
		queryset = Semester_5.objects.all()
		serializer_class = Semester5Serializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)

	def retrieve(self, request, pk=None):
		queryset = Semester_5.objects.all()
		sem = get_object_or_404(queryset, pk=pk)
		serializer = Semester5Serializer(sem)
		return Response(serializer.data)

class Semester6viewSet(ViewSet):
	def list(self, request):
		queryset = Semester_6.objects.all()
		serializer_class = Semester6Serializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)

	def retrieve(self, request, pk=None):
		queryset = Semester_6.objects.all()
		sem = get_object_or_404(queryset, pk=pk)
		serializer = Semester6Serializer(sem)
		return Response(serializer.data)

class Semester7viewSet(ViewSet):
	def list(self, request):
		queryset = Semester_7.objects.all()
		serializer_class = Semester7Serializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)

	def retrieve(self, request, pk=None):
		queryset = Semester_7.objects.all()
		sem = get_object_or_404(queryset, pk=pk)
		serializer = Semester7Serializer(sem)
		return Response(serializer.data)

class Semester8viewSet(ViewSet):
	def list(self, request):
		queryset = Semester_8.objects.all()
		serializer_class = Semester8Serializer(queryset, many=True,context={'request': request})
		return Response(serializer_class.data)

	def retrieve(self, request, pk=None):
		queryset = Semester_8.objects.all()
		sem = get_object_or_404(queryset, pk=pk)
		serializer = Semester8Serializer(sem)
		return Response(serializer.data)

class LoginViewSet(ViewSet):
	def create(self, request):
		serializer_class = LoginSerializer(data = request.data)
		serializer_class.is_valid(raise_exception=True)
		user = serializer_class.validated_data["user"] 
		login(request, user)
		print(request.user.groups.all()[0])
		token, created = Token.objects.get_or_create(user = user)
		return Response({"token":token.key,"user":request.user.username,"Group":request.user.groups.all()[0].name}, status=200)

class StudentInSubjectViewSet(ModelViewSet):
	queryset = add_student_attendance.objects.all()
	serializer_class = AttendancesSerializer

class SeeAttendance(ViewSet):
	def retrieve(self, request, pk=None):
		if(request.user.groups.all()[0].name=="Facultys"):
			attendances = add_student_attendance.objects.filter(subject=pk)
			serializer_class = AttendancesSerializer(attendances,many=True,context={'request': request})
			return Response(serializer_class.data)

		else:
			Student_Data = Students.objects.filter(roll_no=request.user)
			attendances = add_student_attendance.objects.filter( student_name=Student_Data[0],subject=pk)
			serializer_class = AttendancesSerializer(attendances,many=True,context={'request': request})
			return Response(serializer_class.data)
