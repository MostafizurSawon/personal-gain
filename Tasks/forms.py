from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, TaskCategory
from django import forms

class UserSkillForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'

class UserTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'
        fields = ['skill_category', 'topics', 'pending_date' ] 
        
        labels = {
            'skill_category': 'Skill Category',
            'topics': 'Topics',
            'pending_date': 'Pending date',
        }
        
    pending_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
        
class UpdateUserTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'
        fields = ['skill_category','complete', 'topics', 'pending_date', ] 
        
        labels = {
            'skill_category': 'Skill Category',
            'topics': 'Topics',
            'pending_date': 'Pending date',
        }
        
        
