from django.shortcuts import render

from Tasks.models import Task
from UserProfiles.models import UserAccount

# Create your views here.

def home(request):
  tasks = Task.objects.all()
  # ac = UserAccount.objects.all()
  # print("home ac", ac['gender'])
  user_account = request.user.account  # This retrieves the related UserAccount object
  # user_account = request.user.task_account  

  return render(request, 'base.html', {"taskHome": tasks, "ac": user_account})