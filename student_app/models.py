from django.db import models
from courses_app.models import Course
from courses_app.models import Homework
# Create your models here.


'''Student model'''


class Student(models.Model):
    name = models.CharField(max_length=255)
    career = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id}. {self.name}: {self.career}'


'''Homework submission model'''


class Submission(models.Model):
    title = models.CharField(max_length=255)
    statement = models.CharField(max_length=1000)
    homework = models.ForeignKey(Homework, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    grade = models.FloatField(blank=True, default=None, null=True)

    def __str__(self):
        return f'Homework submission {self.id}: {Student.objects.get(id=self.owner.id).name}'
