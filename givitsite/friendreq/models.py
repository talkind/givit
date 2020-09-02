from django.db import models

# Create your models here.
REGION_CHOICES = [
    ('Tel Aviv','Tel Aviv'),
    ('Jerusalem','Jerusalem'),
    ('Beer Sheva','Beer Sheva'),
    ('Haifa','Haifa'),
    ('Modiin','Modiin'),
    ('Hasharon','Hasharon'),
]

ITEM_CHOICES = [
    ('ארון','closet'),
    ('מיטה','bed'),
    ('כיסא', 'chair'),
    ('מקרר','fridge'),
    ('מכונת כביסה','Washing machine'),
    ('ספה','sofa'),
    

]
STATUS_CHOICES = [
    ('open','open'),
    ('closed','closed'),
]

class ItemRequest(models.Model):
    #friennd ID inherite from user table
    friend_id = models.IntegerField(default = 305355356)
    item = models.CharField(max_length = 40,choices = ITEM_CHOICES, default='ארון')
    region = models.CharField(max_length = 40,choices = REGION_CHOICES, default='Tel Aviv')
    special_req= models.TextField()
    status = models.CharField(max_length = 40,default = 'open', choices = STATUS_CHOICES)
    
    
class ItemsFound(models.Model):
    request_id = models.IntegerField()
    url = models.URLField()
    picture = models.URLField()
    city = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
