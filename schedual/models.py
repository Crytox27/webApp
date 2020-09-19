from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [('tr', 'Teacher'), ('sf', "Staff"), ('gt', "Guest")]
    role_name = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default='gt',
    )
    def __str__(self):
        return self.user.username

class Discipline(models.Model):
    name = models.CharField(max_length=20)
    teachers = models.ManyToManyField('Profile', related_name='disciplines')
    groups = models.ManyToManyField('Group', related_name='disciplines')
    lessons_count = models.IntegerField()
    computers = models.BooleanField()
    projector = models.BooleanField()
    def __str__(self):
        return self.name

class Wish(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='wishes')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='wishes')
    auditories = models.ManyToManyField('Auditory', related_name='wishes')
    # lesson_time
    def __str__(self):
        return self.discipline.name

# class Role(models.Model):
#     ROLE_CHOICES = [('tr', 'Teacher'), ('sf', "Staff"), ('gt', "Guest")]
#     role_name = models.CharField(
#         max_length=2,
#         choices=ROLE_CHOICES,
#         default='gt',
#     )

class Auditory(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    computers = models.BooleanField()
    projector = models.BooleanField()
    def __str__(self):
        return str(self.number)

class Group(models.Model):
    number = models.IntegerField()
    student_number = models.IntegerField()
    def __str__(self):
        return str(self.number)
