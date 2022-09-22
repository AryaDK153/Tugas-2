from django.db import models

# Create your models here.
class AttributeWatchList(models.Model):
    title = models.CharField(max_length=50)
    watched = models.CharField(max_length=10)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=10)
    review = models.TextField()