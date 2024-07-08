from django.db import models

# Create your models here.
class Visit (models.Model):
    # id -> hidden
    path = models.TextField(blank=True, null=True) # col
    timeStamp = models.DateTimeField(auto_now_add=True) #col