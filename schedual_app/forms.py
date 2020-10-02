from django import forms
from .models import *

class AddTeachers(forms.Form):
    full_name = forms.CharField(label="Name", max_length=200)
    project = forms.ModelChoiceField(queryset=SchedualProject.objects.all())

class AddGroups(forms.Form):
    number = forms.IntegerField()
    year = forms.IntegerField()
    division = forms.IntegerField()
    group = forms.IntegerField()
    student_number = forms.IntegerField()
    project = forms.ModelChoiceField(queryset=SchedualProject.objects.all())

class AddAuditories(forms.Form):
    number = forms.IntegerField()
    capacity = forms.IntegerField()
    computers = forms.BooleanField(required=False)
    projector = forms.BooleanField(required=False)
    project = forms.ModelChoiceField(queryset=SchedualProject.objects.all())

class AddDisciplines(forms.Form):
    name = forms.CharField()
    teachers = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Teacher.objects.all())
    groups = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Group.objects.all())
    lessons_count = forms.IntegerField()
    computers = forms.BooleanField(required=False)
    projector = forms.BooleanField(required=False)
    project = forms.ModelChoiceField(queryset=SchedualProject.objects.all())

class StaffHome(forms.Form):
    option_choices = (
        ('DS', 'Disciplines'),
        ('GR', 'Groups'),
        ('AD', 'Auditories'),
        ('TC', 'Teachers'),
    )
    project = forms.ModelChoiceField(queryset=SchedualProject.objects.all())
    options = forms.MultipleChoiceField(choices=option_choices, widget=forms.CheckboxSelectMultiple())

    def only_option(self):
        if len(self.cleaned_data['options']) > 1:
            raise forms.ValidationError('Select only 1 option.')
        return self.cleaned_data['options']
