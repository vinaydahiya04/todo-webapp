from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             default='blank', related_name='todolist', null=True)
    name = models.CharField( max_length=50)
    detail = models.TextField()
    status = models.BooleanField(default = False)
    target_date = models.DateField()

    def completed(self,*args,**kwargs):
        self.status = True 
        self.save(*args,*kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('todoapp:task_list')
