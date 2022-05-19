import json

from django.http import JsonResponse
from django.views import View
from courses_app.models import Course, Homework
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class CourseView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get(self, request, course_id):
        data = list(Course.objects.filter(id=course_id).values())
        return JsonResponse({'message': data})


class HomeworkView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, course_id):
        data = list(Homework.objects.filter(course_id=course_id).values())
        return JsonResponse({'message': data})

    def post(self, request):
        data = json.loads(request.body)
        Homework.objects.create(
            title=data['title'],
            statement=data['statement'],
            course_id=data['course_id']
        )
        return JsonResponse({'message': 'Successful, homework created'})
