from django.db import models
from django.utils import timezone
# Create your models here.

def one_week_hence():

    return timezone.now() + timezone.timedelta(days=7)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=one_week_hence)


    def __str__(self):
        return self.title
    