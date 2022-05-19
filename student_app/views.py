import json

from django.http import JsonResponse
from django.views import View
from student_app.models import Student, Submission
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class StudentView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, course_id):
        data = Student.objects.filter(course_id=course_id).values()
        return JsonResponse({'message': list(data)})


class SubmissionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_course):
        data = Submission.objects.filter(homework=id_course).values()
        return JsonResponse({'message': list(data)})

    def post(self, request):
        data = json.loads(request.body)
        Submission.objects.create(
            title=data['title'],
            statement=data['statement'],
            homework_id=data['homework_id'],
            owner_id=data['owner_id']
        )
        return JsonResponse({'message': 'Successful, homework submission send'})

    def put(self, request, id_submission):
        data = json.loads(request.body)
        submission = Submission.objects.get(id=id_submission)
        submission.grade = data['grade']
        submission.save()

        return JsonResponse({'message': 'Successful, homework submission graded'})
