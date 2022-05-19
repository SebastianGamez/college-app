from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from teachers_app.models import Teacher


# Create your views here.


'''Teacher view'''


class TeacherView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, teacher_id):
        data = Teacher.objects.filter(id=teacher_id).values()
        return JsonResponse({'message': list(data)})
