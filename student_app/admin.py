from django.contrib import admin
from student_app.models import Student, Submission

# Register your models here.

'''student register'''

admin.site.register(Student)
admin.site.register(Submission)
