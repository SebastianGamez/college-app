from django.urls import path
from teachers_app.views import TeacherView

urlpatterns = [
    path('<int:teacher_id>/', TeacherView.as_view(), name='teacher')
]
