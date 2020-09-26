from django import forms
from .models import *

class AddTeachers(forms.Form):
    full_name = forms.CharField(label="Name", max_length=200)

class AddGroups(forms.Form):
    number = forms.IntegerField()
    year = forms.IntegerField()
    division = forms.IntegerField()
    group = forms.IntegerField()
    student_number = forms.IntegerField()

class AddAuditories(forms.Form):
    number = forms.IntegerField()
    capacity = forms.IntegerField()
    computers = forms.BooleanField(required=False)
    projector = forms.BooleanField(required=False)

class AddDisciplines(forms.Form):
    name = forms.CharField()
    teachers = forms.ModelMultipleChoiceField(queryset=Teacher.objects.all())
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all())
    lessons_count = forms.IntegerField()
    computers = forms.BooleanField(required=False)
    projector = forms.BooleanField(required=False)
    project = forms.ModelChoiceField(queryset=SchedualProject.objects.all())
