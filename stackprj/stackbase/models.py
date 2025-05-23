from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    content= models.TextField(null=True, blank=True)
    data_created = models.DateTimeField(default=timezone.now)

 
    
    def __str__(self):
        return f'{self.user.username} - Question'
