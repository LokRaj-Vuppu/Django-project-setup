from celery import shared_task

@shared_task
def add(x, y):
    print('received task - add')
    return x + y
