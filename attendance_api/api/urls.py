from django.conf.urls import url, include
from rest_framework import routers
from . import views
from django.urls import path

router = routers.DefaultRouter()
router.register(r'login',views.LoginViewSet,basename='user')
router.register(r'dashboard',views.DashBoardViewSet,basename='dashboard')
router.register(r'professers', views.FacultysViewSet,basename='professers')
router.register(r'students', views.StudentsViewSet,basename='students')
router.register(r'attendances',views.AttendancesViewSet,basename='attendances')
router.register(r'sem-1',views.Semester1viewSet,basename='sem_1')
router.register(r'sem-2',views.Semester2viewSet,basename='sem_2')
router.register(r'sem-3',views.Semester3viewSet,basename='sem_3')
router.register(r'sem-4',views.Semester4viewSet,basename='sem_4')
router.register(r'sem-5',views.Semester5viewSet,basename='sem_5')
router.register(r'sem-6',views.Semester6viewSet,basename='sem_6')
router.register(r'sem-7',views.Semester7viewSet,basename='sem_7')
router.register(r'sem-8',views.Semester8viewSet,basename='sem_8')
router.register(prefix=r'enroll-students/(?P<sem_id>\d+)', viewset=views.StudentInSubjectViewSet, base_name='request')
router.register(r'add-attendance',views.StudentInSubjectViewSet,basename='add_attendance')
router.register(r'attendance', viewset=views.SeeAttendance, base_name='request')



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    path('enroll-students/3',views.StudentInSubjectViewSet.as_view({'get': 'list'}),name='u'),
    url(r'^professers', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]