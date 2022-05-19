from django.db import models
from courses_app.models import Course
# Create your models here.


'''Teacher model'''


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id}. {self.name}: {Course.objects.get(id=self.course.id).name}'
