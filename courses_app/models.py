from django.db import models

# Create your models here.


'''Course model'''


class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}({self.id}): Departamento de {self.department}'


'''Homework model'''


class Homework(models.Model):
    title = models.CharField(max_length=255)
    statement = models.CharField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Homework ({self.id}): {Course.objects.get(id=self.course.id).name}'