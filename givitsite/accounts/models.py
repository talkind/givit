from django.db import models
from django.contrib.auth.models import User

MEMBERSHIP_TYPE = [
    ('friend','friend'),
    ('coordinator','coordinator'),
]

DEGREE = [
    ('BA', 'BA'),
    ('BSC', 'BSC'),
    ('MA', 'MA'),
    ('MSC', 'MSC'),
    ('PHD', 'PHD'),
]

FIELD_OF_STUDY = [
    ('Computer Science', 'Computer Science'),
    ('Business', 'Business'),
    ('Sustainability', 'Sustainability'),
    ('Communications', 'Communications'),
    ('Economics', 'Economics'),
    ('Law', 'Law'),
    ('Psychology', 'Communications'),
    ('Government, Diplomacy and Strategy', 'Government, Diplomacy and Strategy'),
]

GENDER = [
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    confirmed = models.BooleanField("confirmed", default=False)
    student_id = models.IntegerField(help_text='ID OR passport no.')
    gender = models.CharField(max_length=10, default='other', choices=GENDER)
    phone_number = models.IntegerField(help_text='example: 0505551234')
    date_of_birth = models.DateField(help_text='mm/dd/yyyy')
    home_address = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100, choices=FIELD_OF_STUDY)
    degree = models.CharField(max_length=100, default='BA', choices = DEGREE)
    scholarship = models.CharField(max_length=100)
    membership_type = models.CharField(max_length=100, default= 'friend', choices=MEMBERSHIP_TYPE)

    def _str_(self):
        return self.user.username
