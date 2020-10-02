from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("addTeachers/", views.addTeachers, name="addTeachers"),
path("addGroups/", views.addGroups, name="addGroups"),
path("addAuditories/", views.addAuditories, name="addAuditories"),
path("addDisciplines/", views.addDisciplines, name="addDisciplines"),
path("viewDisciplines/<int:id>/", views.viewDisciplines, name="viewDisciplines"),
path("viewGroups/<int:id>/", views.viewGroups, name="viewGroups"),
path("viewAuditories/<int:id>/", views.viewAuditories, name="viewAuditories"),
path("viewTeachers/<int:id>/", views.viewTeachers, name="viewTeachers"),
path("staffHome/", views.staffHome, name="staffHome"),
]
