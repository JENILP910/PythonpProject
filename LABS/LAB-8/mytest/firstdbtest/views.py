

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from .models import Student


def index(request):
    return render(request,'addstudentinfo.html')


def getstudentinfo(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'addstudentinfo.html', c)


def addstudentinfo(request):
    sname = request.POST.get('studentname', '')
    sdate = request.POST.get('birthdate', '')
    s = Student(student_name = sname, student_dob=sdate)
    s.save()
    return render(request, 'addrecord.html')


def addsuccess(request):
    return render(request, 'addrecord.html')

 
def StudentListView(request):
    stu=Student.objects.all()
    return render(request,'student_list.html',{'student_list':stu})


def delstudent(request):
    sname = request.POST.get('studentname', '')
    Student.objects.filter(student_name=sname).delete()
    return render(request, 'addstudentinfo.html')