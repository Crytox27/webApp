from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    profile = models.OneToOneField('Profile', on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey('SchedualProject', on_delete=models.CASCADE, null=True, related_name='teachers')

    def __str__(self):
        return self.full_name


class Discipline(models.Model):
    name = models.CharField(max_length=20)
    teachers = models.ManyToManyField('Teacher', related_name='disciplines', blank=True)
    groups = models.ManyToManyField('Group', related_name='disciplines', blank=True)
    lessons_count = models.IntegerField()
    computers = models.BooleanField()
    projector = models.BooleanField()
    project = models.ForeignKey('SchedualProject', on_delete=models.CASCADE, null=True, related_name='disciplines')

    def __str__(self):
        return self.name

class Wish(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='wishes')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='wishes')
    auditories = models.ManyToManyField('Auditory', related_name='wishes')
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    first_lesson = models.BooleanField(default=False)
    second_lesson = models.BooleanField(default=False)
    third_lesson = models.BooleanField(default=False)
    fourth_lesson = models.BooleanField(default=False)
    fifth_lesson = models.BooleanField(default=False)
    sixth_lesson = models.BooleanField(default=False)
    seventh_lesson = models.BooleanField(default=False)
    project = models.ForeignKey('SchedualProject', on_delete=models.CASCADE, null=True, related_name='wishes')

    def __str__(self):
        return self.discipline.name

class Role(models.Model):
    role_name = models.CharField(max_length=200)
    staff_credentials = models.BooleanField(default=False)
    teacher_credentials = models.BooleanField(default=False)
    guest_credentials = models.BooleanField(default=True)


    def __str__(self):
        return self.role_name

class Auditory(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    computers = models.BooleanField()
    projector = models.BooleanField()
    project = models.ForeignKey('SchedualProject', on_delete=models.CASCADE, null=True, related_name='auditories')

    def __str__(self):
        return str(self.number)

class Group(models.Model):
    number = models.IntegerField()
    year = models.IntegerField(default=1)
    division = models.IntegerField(default=1)
    group = models.IntegerField(default=1)
    student_number = models.IntegerField()
    project = models.ForeignKey('SchedualProject', on_delete=models.CASCADE, null=True, related_name='groups')

    def __str__(self):
        return str(self.number)

class SchedualProject(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)
