from django.db import models

# Create your models here.

def upload_user_files(instance, filename):
    # Upload function to determine storage location
    return f'user_files/{filename}'

class TestFileUploads(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    user_docs = models.FileField(upload_to=upload_user_files, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.user_docs} - {self.created_at}'

