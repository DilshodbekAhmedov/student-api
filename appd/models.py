from django.db import models
from .verbose import val

class Teacher(models.Model):

    class TeacherManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=True)


    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, validators=[val])
    status = models.BooleanField(default=False)
    objects = models.Manager()
    teacher_objects = TeacherManager()



    class Meta:
        ordering = ["id"]


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, validators=[val])