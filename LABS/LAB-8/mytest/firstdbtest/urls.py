

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studentinfo', views.addstudentinfo, name='add'),
    path('getinfo', views.getstudentinfo, name='add'),
    path('remove', views.delstudent, name ='remove'),
    url('students', views.StudentListView, name ='students'),
]