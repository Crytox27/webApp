from django.shortcuts import render, redirect
from .forms import *
from .models import *

def home(response):
    return render(response, "schedual_app/home.html", {})

def addTeachers(response):
    if response.method == "POST":
        form = AddTeachers(response.POST)
        if form.is_valid():
            n = form.cleaned_data["full_name"]
            project = form.cleaned_data["project"]
            tmp = Teacher(full_name=n, project=project)
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
            project = form.cleaned_data["project"]
            tmp = Group(number=n, year=y, division=d, group=g, student_number=s, project=project)
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
            project = form.cleaned_data["project"]
            tmp = Auditory(number=n, capacity=cap, computers=com, projector=p, project=project)
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
            tmp = Discipline.objects.create(name=n, lessons_count=lc, computers=c, projector=projector, project=project)
            teachers_tmp = Teacher.objects.filter(id__in=t)
            groups_tmp = Group.objects.filter(id__in=gr)
            # tmp.teachers.set(teachers_tmp)
            # tmp.groups.set(groups_tmp)
            for ts in teachers_tmp:
                tmp.teachers.add(ts)
            for gs in groups_tmp:
                tmp.groups.add(gs)
            # tmp.teachers = t
            # tmp.groups = gr
            tmp.save()
    else:
        form = AddDisciplines()
    return render(response, "schedual_app/addDisciplines.html", {"form":form})

def staffHome(response):
    if response.method == "POST":
        form = StaffHome(response.POST)
        if form.is_valid():
            pr = form.cleaned_data["project"]
            opt = form.only_option()
            print(opt)
            if opt == ['DS']:
                return redirect("/viewDisciplines/%d/"%pr.id)
            elif opt == ['GR']:
                return redirect("/viewGroups/%d/"%pr.id)
            elif opt == ['AD']:
                return redirect("/viewAuditories/%d/"%pr.id)
            elif opt == ['TC']:
                return redirect("/viewTeachers/%d/"%pr.id)
            # n = form.cleaned_data["name"]
            # t = form.cleaned_data["teachers"]
            # gr = form.cleaned_data["groups"]
            # lc = form.cleaned_data["lessons_count"]
            # c = form.cleaned_data["computers"]
            # projector = form.cleaned_data["projector"]
            # project = form.cleaned_data["project"]
            # tmp = Discipline.objects.create(name=n, lessons_count=lc, computers=c, projector=projector, project=project)
            # teachers_tmp = Teacher.objects.filter(id__in=t)
            # groups_tmp = Group.objects.filter(id__in=gr)
            # tmp.teachers.set(teachers_tmp)
            # tmp.groups.set(groups_tmp)
            # for ts in teachers_tmp:
            #     tmp.teachers.add(ts)
            # for gs in groups_tmp:
            #     tmp.groups.add(gs)
            # tmp.teachers = t
            # tmp.groups = gr
            # tmp.save()
    else:
        form = StaffHome()
    return render(response, "schedual_app/staffHome.html", {"form":form})

def viewDisciplines(response, id):
    proj = SchedualProject.objects.get(id=id)
    return render(response, "schedual_app/viewDisciplines.html", {"proj":proj})

def viewGroups(response, id):
    proj = SchedualProject.objects.get(id=id)
    return render(response, "schedual_app/viewGroups.html", {"proj":proj})

def viewAuditories(response, id):
    proj = SchedualProject.objects.get(id=id)
    return render(response, "schedual_app/viewAuditories.html", {"proj":proj})

def viewTeachers(response, id):
    proj = SchedualProject.objects.get(id=id)
    return render(response, "schedual_app/viewTeachers.html", {"proj":proj})
