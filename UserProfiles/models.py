from django.db import models
from django.contrib.auth.models import User
from Tasks.models import Task
import random



class JobName(models.Model):
  name = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name

class UserAccount(models.Model):
    GENDER_CHOICES = [
      ('Male', 'Male'),
      ('Female', 'Female'),
    ]
    TYPE_CHOICES = [
      ('Super', 'Super'),
      ('Regular', 'Regular'),
      ('Below Average', 'Below Average'),
    ]
    
    JOB_CHOICES = [
      ('Student', 'Student'),
      ('Job Holder', 'Job Holder'),
      ('Unemployed', 'Unemployed'),
      ('Both', 'Both'),
    ]
    
    COUNTRY_CHOICES = [
      ('Bangladesh','BD'),
      ('Other', 'Other'),
    ]
    
    images = [
      'https://img.freepik.com/free-photo/androgynous-avatar-non-binary-queer-person_23-2151100207.jpg',
      'https://img.freepik.com/free-photo/cartoon-character-with-handbag-sunglasses_71767-99.jpg',
      'https://img.freepik.com/free-photo/anime-style-character-space_23-2151134190.jpg', 
      'https://img.freepik.com/premium-photo/poster-anime-character-with-fiery-background_943629-32000.jpg',
      'https://img.freepik.com/free-photo/androgynous-avatar-non-binary-queer-person_23-2151100183.jpg'
      ]
    
    # print(random.choice(images))
  
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, blank=True, choices=TYPE_CHOICES, default="Regular")
    # task = models.ManyToManyField(Task, related_name="tasks")
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.URLField(blank=True, null=True, default=random.choice(images))
    gender = models.CharField(max_length=20, blank=True, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=14, blank=True)
    points = models.IntegerField(null=True, blank=True, default=0)
    age = models.IntegerField(null=True, blank=True)
    hometown = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)
    job=models.CharField(max_length=20, blank=True, null=True, choices=JOB_CHOICES)
    country=models.CharField(max_length=20, blank=True, null=True, choices=COUNTRY_CHOICES)
    position = models.OneToOneField(JobName,on_delete=models.CASCADE, blank=True, null=True)
    company = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return self.user.first_name
    
    
class UserSocialAccount(models.Model):
  facebook = models.URLField(blank=True, null=True)
  youtube = models.URLField(blank=True, null=True)
  linkedin = models.URLField(blank=True, null=True)
  github = models.URLField(blank=True, null=True)
  x = models.URLField(blank=True, null=True)
  portfolio = models.URLField(blank=True, null=True)
  user = models.OneToOneField(User, related_name='social_account', on_delete=models.CASCADE)
  
  def __str__(self):
    return self.user.username
  
  
class UserEducation(models.Model):
  SUBJECT_CHOICES=[
    ('CSE', 'CSE'),
    ('EEE', 'EEE'),
    ('LLB', 'LLB'),
    ('CIVIL', 'CIVIL'),
    ('BBA', 'BBA'),
    ('OTHERS', 'OTHERS'),
  ]
  
  BACKGROUND_CHOICES=[
    ('CSE', 'CSE'),
    ('NON-CS', 'NON-CS'),
  ]
  
  GROUP_CHOICE=[
    ('SCIENCE', 'SCIENCE'),
    ('ARTS', 'ARTS'),
    ('COMMERCE', 'COMMERCE'),
  ]
  
  last_education = models.CharField(max_length=50, blank=True, null=True)
  subject = models.CharField(max_length=20, blank=True, null=True, choices=SUBJECT_CHOICES)
  background = models.CharField(max_length=20, blank=True, null=True, choices=BACKGROUND_CHOICES)
  year = models.IntegerField(null=True, blank=True)
  result = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=8)
  ssc_school=models.CharField(max_length=30,null=True, blank=True)
  ssc_year=models.IntegerField(null=True, blank=True)
  ssc_subject = models.CharField(max_length=20, blank=True, null=True, choices=GROUP_CHOICE)
  hsc_school=models.CharField(max_length=30,null=True, blank=True)
  hsc_year=models.IntegerField(null=True, blank=True)
  hsc_subject = models.CharField(max_length=20, blank=True, null=True, choices=GROUP_CHOICE)
  university=models.CharField(max_length=30,null=True, blank=True)
  university_year=models.IntegerField(null=True, blank=True)
  bootcamp=models.CharField(max_length=50,null=True, blank=True)
  user = models.OneToOneField(User, related_name='user_education', on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.user.username}'s Education" 
  
