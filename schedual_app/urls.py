from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("addTeachers/", views.addTeachers, name="addTeachers"),
path("addGroups/", views.addGroups, name="addGroups"),
path("addAuditories/", views.addAuditories, name="addAuditories"),
path("addDisciplines/", views.addDisciplines, name="addDisciplines"),
]
