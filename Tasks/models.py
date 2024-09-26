from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskCategory(models.Model):
  skill = models.CharField(max_length=20, null=True, blank=True)
  
  def __str__(self):
    return self.skill
  
class Task(models.Model):
  user = models.ForeignKey(User, related_name='task_account', on_delete=models.CASCADE,default=2)
  skill_category = models.ManyToManyField(TaskCategory, related_name="Task_skill", blank=True)
  topics = models.TextField(blank=True, null=True, help_text="The topics you have learned. (Separate by Comma.)")
  complete = models.BooleanField(default=False, blank=True)
  pending_date = models.DateTimeField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  
  def __str__(self):
    return f"{self.user.username}'s task."