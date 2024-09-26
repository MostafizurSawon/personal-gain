from django.shortcuts import render

from Tasks.models import Task
from UserProfiles.models import UserAccount

# Create your views here.

def home(request):
  tasks = Task.objects.filter(user=request.user)
  ac = UserAccount.objects.all()
  print("home ac", ac['gender'])
  return render(request, 'base.html', {"taskHome": tasks, "ac": ac})