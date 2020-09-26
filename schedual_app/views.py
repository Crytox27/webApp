from django.shortcuts import render
from .forms import *
from .models import *

def home(response):
    return render(response, "schedual_app/home.html", {})

def addTeachers(response):
    if response.method == "POST":
        form = AddTeachers(response.POST)
        if form.is_valid():
            n = form.cleaned_data["full_name"]
            tmp = Teacher(full_name=n)
            tmp.save()
    else:
        form = AddTeachers()
    return render(response, "schedual_app/addTeachers.html", {"form":form})

def addGroups(response):
    if response.method == "POST":
        form = AddGroups(response.POST)
        if form.is_valid():
            n = form.cleaned_data["number"]
            y = form.cleaned_data["year"]
            d = form.cleaned_data["division"]
            g = form.cleaned_data["group"]
            s = form.cleaned_data["student_number"]
            tmp = Group(number=n, year=y, division=d, group=g, student_number=s)
            tmp.save()
    else:
        form = AddGroups()
    return render(response, "schedual_app/addGroups.html", {"form":form})

def addAuditories(response):
    if response.method == "POST":
        form = AddAuditories(response.POST)
        if form.is_valid():
            n = form.cleaned_data["number"]
            cap = form.cleaned_data["capacity"]
            com = form.cleaned_data["computers"]
            p = form.cleaned_data["projector"]
            tmp = Auditory(number=n, capacity=cap, computers=com, projector=p)
            tmp.save()
    else:
        form = AddAuditories()
    return render(response, "schedual_app/addAuditories.html", {"form":form})

def addDisciplines(response):
    if response.method == "POST":
        form = AddDisciplines(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = form.cleaned_data["teachers"]
            gr = form.cleaned_data["groups"]
            lc = form.cleaned_data["lessons_count"]
            c = form.cleaned_data["computers"]
            projector = form.cleaned_data["projector"]
            project = form.cleaned_data["project"]
            tmp = Discipline(name=n, teachers.set()=t, groups.set()=gr, lessons_count=lc, computers=c, projector=projector, project=project)
            tmp.save()
    else:
        form = AddDisciplines()
    return render(response, "schedual_app/addDisciplines.html", {"form":form})
