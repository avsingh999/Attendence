
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^', include('attendance.urls')),
    url(r'^admin/', admin.site.urls),
]
