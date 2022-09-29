from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()