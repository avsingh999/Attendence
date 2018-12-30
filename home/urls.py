
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^student_login/$', views.student_login, name="student_login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^dashboard/$', views.dashboard_faculty, name="dashboard"),
    url(r'^add_student/$', views.add_student, name="add_student"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
