from django.http import HttpResponse
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from UserProfiles.models import UserAccount
from .forms import UserTaskForm, UserSkillForm, UpdateUserTaskForm, UserSkillForm
from .models import Task, TaskCategory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Assuming you're using the default User model

# Create your views here.
@login_required
def update_category_form(request):
    try:
        data = get_object_or_404(TaskCategory, user=request.user)

        if request.method == "POST":
            data_form = UserSkillForm(request.POST, instance=data)

            if data_form.is_valid():
                data_form.save()
                messages.success(request, "Task category data updated successfully!")
                return redirect("profile")
            else:
                context = {
                    "form": data_form,
                    "type": "Update"
                }
                return render(request, "add-info.html", context=context)

        data_form = UserSkillForm(instance=data)
        context = {
            "form": data_form,
            "type": "Update"
        }
        return render(request, "add-info.html", context=context)
    except TaskCategory.DoesNotExist:
        return HttpResponse("Task category Data does not exist")
    
@login_required
def add_task_form(request):
    if request.method == "POST":
        form = UserTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
        else:
            return render(request, "add-info.html", {"form": form})
    else:
        form = UserTaskForm()
        return render(request, "add-info.html", {"form": form})
    
@login_required
def add_task_form(request):
    if request.method == "POST":
        form = UserTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Don't save yet, modify the object first
            task.user = request.user        # Assign the logged-in user
            task.save()                     # Now save the task
          
            user_account = UserAccount.objects.get(user=request.user)
            user_account.points += 20
            user_account.save()

            return redirect("profile")
        else:
            return render(request, "add-info.html", {"form": form, "type": "Add new Task"})
    else:
        form = UserTaskForm()
        return render(request, "add-info.html", {"form": form, "type": "Add new Task"})

    
@login_required
def add_category_form(request):
    if request.method == "POST":
        form = UserSkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
        else:
            return render(request, "add-info.html", {"form": form, "type": "Add Category"})
    else:
        form = UserSkillForm()
        return render(request, "add-info.html", {"form": form, "type": "Add Category"})
      
      
# @login_required
# def update_task_form(request, pk):
#     try:
#         data = get_object_or_404(Task, user=request.user, pk=pk)

#         if request.method == "POST":
#             data_form = UpdateUserTaskForm(request.POST, instance=data)

#             if data_form.is_valid():
#                 data_form.save()
#                 messages.success(request, "Task data updated successfully!")
#                 return redirect("profile")
#             else:
#                 context = {
#                     "form": data_form,
#                     "type": "Update"
#                 }
#                 return render(request, "add-info.html", context=context)

#         data_form = UpdateUserTaskForm(instance=data)
#         context = {
#             "form": data_form,
#             "type": "Update"
#         }
#         return render(request, "add-info.html", context=context)
#     except Task.DoesNotExist:
#         return HttpResponse("Task Data does not exist")

@login_required
def update_task_form(request, pk):
    try:
        # Get the task associated with the logged-in user
        task = get_object_or_404(Task, user=request.user, pk=pk)

        # Store the initial value of 'complete' before form submission
        was_complete = task.complete

        if request.method == "POST":
            data_form = UpdateUserTaskForm(request.POST, instance=task)

            if data_form.is_valid():
                # Save the updated task
                updated_task = data_form.save()

                # Check if the 'complete' status has changed from False to True
                if not was_complete and updated_task.complete:
                    # Fetch the user's account and add 5 points
                    user_account = get_object_or_404(UserAccount, user=request.user)
                    user_account.points += 5
                    user_account.save()

                # Success message and redirect after saving
                messages.success(request, "Task updated successfully!")
                return redirect("profile")
            else:
                # If form is not valid, render the form again with errors
                context = {
                    "form": data_form,
                    "type": "Update"
                }
                return render(request, "add-info.html", context=context)

        # Initialize the form with the current task instance
        data_form = UpdateUserTaskForm(instance=task)
        context = {
            "form": data_form,
            "type": "Update"
        }
        return render(request, "add-info.html", context=context)

    except Task.DoesNotExist:
        return HttpResponse("Task does not exist.")