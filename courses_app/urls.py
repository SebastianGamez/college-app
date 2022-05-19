from django.urls import path
from courses_app.views import CourseView, HomeworkView

urlpatterns = [
    path('<int:course_id>/', CourseView.as_view(), name='get_course'),
    path('homework/', HomeworkView.as_view(), name='post_homework'),
    path('homework/<int:course_id>/', HomeworkView.as_view(), name='get_homeworks'),
]
