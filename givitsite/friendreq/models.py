from django.db import models

# Create your models here.

class ItemRequest(models.Model):
    item = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40)
    special_req= models.TextField()