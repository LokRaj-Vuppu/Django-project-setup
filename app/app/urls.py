from django.contrib import admin
from django.urls import path
from core.views import home, check_task_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('status/<str:task_id>/', check_task_status, name='check_task_status'),
]
