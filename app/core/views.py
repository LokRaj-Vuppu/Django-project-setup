from django.http import HttpResponse
from django.shortcuts import render
from core.models import TestFileUploads
from core.tasks import add
from celery.result import AsyncResult
from django.http import JsonResponse
# Create your views here.

def home(request):
    try:
        # execute celery task
        result = add.delay(12,12)
        task_call = {'task_id': result.id, 'status': 'Task submitted', 'result': result}
        print('task_call', task_call)
        # end celery
        all_uploaded_files = TestFileUploads.objects.all()
        if request.method == 'POST':
            username = request.POST.get('username')
            uploaded_file = request.FILES.get('uploaded_file')
            TestFileUploads.objects.create(name=username, user_docs=uploaded_file)
            
            return render(request, 'core/home.html', {'all_uploaded_files': all_uploaded_files})
        else:
            return render(request, 'core/home.html',  {'all_uploaded_files': all_uploaded_files})
    except Exception as error:
        print(f'Exception in home- file upload - {error}')
        return HttpResponse(f'<h1>Something went wrong</h1> - {error}')


def check_task_status(request, task_id):
    result = AsyncResult(task_id)
    return JsonResponse({'task_id': task_id, 'status': result.status, 'result': result.result})