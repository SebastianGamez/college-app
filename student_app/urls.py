from django.urls import path
from student_app.views import StudentView, SubmissionView

urlpatterns = [
    path('<int:course_id>/', StudentView.as_view(), name='get_students'),
    path('submission/<int:id_course>/', SubmissionView.as_view(), name='get_submissions'),
    path('submission/grade/<int:id_submission>/', SubmissionView.as_view(), name='put_submissions'),
    path('submission/', SubmissionView.as_view(), name='post_submissions')
]
