from django.http import HttpResponse
from django.views.generic import FormView
from .forms import UserEducationForm, UserRegistrationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm, UserJobForm, UserSocialForm
from .models import UserAccount, UserEducation, UserSocialAccount
from Tasks.models import Task
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User  # Assuming you're using the default User model

@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    # When a new User is created, create the corresponding UserAccount
    if created:
        UserAccount.objects.create(
            user=instance, 
            image=random.choice(UserAccount.images),  # Or handle image selection appropriately
        )
        UserSocialAccount.objects.create(
            user=instance, 
        )
        UserEducation.objects.create(
            user=instance,   
        )


# User Authentication starts here

from django.db import IntegrityError

class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()  # Save the user from the form

        # Check and create UserAccount if it doesn't already exist
        if not UserAccount.objects.filter(user=user).exists():
            try:
                UserAccount.objects.create(
                    user=user,
                    image=random.choice(UserAccount.images),
                )
            except IntegrityError:
                form.add_error(None, "User account already exists.")
                return self.form_invalid(form)

        # Check and create UserSocialAccount if it doesn't already exist
        if not UserSocialAccount.objects.filter(user=user).exists():
            try:
                UserSocialAccount.objects.create(user=user)
            except IntegrityError:
                form.add_error(None, "User social account already exists.")
                return self.form_invalid(form)
            
        # Check and create UserSocialAccount if it doesn't already exist
        if not UserEducation.objects.filter(user=user).exists():
            try:
                UserEducation.objects.create(user=user)
            except IntegrityError:
                form.add_error(None, "User Education already exists.")
                return self.form_invalid(form)
        
        return super().form_valid(form)

    
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    
    def get_success_url(self):
        # print("logged")
        return reverse_lazy('profile')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# User Authentication ends here



# Profile Section starts here
@login_required
def MyProfile(request):
#   data = UserAccount.objects.all()
    data = get_object_or_404(UserAccount, user=request.user)
    social = get_object_or_404(UserSocialAccount, user=request.user)
    edu = get_object_or_404(UserEducation, user=request.user)
    tasks = Task.objects.filter(user=request.user)
    a = Task.objects.filter(user=request.user)
    c = tasks.filter(complete=True, user=request.user)
    p = tasks.filter(complete=False, user=request.user)
    complete = request.GET.get("complete")
    print(complete)
    if complete == "1":
        tasks = tasks.filter(complete=True, user=request.user)
    elif complete == "0":
        tasks = tasks.filter(complete=False, user=request.user)
    print("hello",data)
    if data:
        return render(request, 'profile.html',  {'data': data, 'social': social, 'edu':edu, 'tasks': tasks, 'complete':len(c), 'pending':len(p), 'all':len(a)})
    else:
        return render(request, 'profile.html')

@login_required
def add_profile_info_form(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # if UserAccount.objects.filter(name=request.user).exists():
            #     messages.error(request, "You cannot add more data. An entry already exists for your account.")
            #     return render(request, "add-info.html", {"form": form, "type": "Add"})
            
            form.instance.user = request.user
            form.save()
            messages.success(request, "Data added successfully!")
            return redirect("home")
    else:
        form = UserProfileForm()

    return render(request, "add-info.html", {"form": form, "type": "Add"})

@login_required
def add_social_form(request):
    if request.method == "POST":
        form = UserSocialForm(request.POST)
        if form.is_valid():
            # if UserAccount.objects.filter(name=request.user).exists():
            #     messages.error(request, "You cannot add more data. An entry already exists for your account.")
            #     return render(request, "add-info.html", {"form": form, "type": "Add"})
            
            form.instance.user = request.user
            form.save()
            messages.success(request, "Social data added successfully!")
            return redirect("profile")
    else:
        form = UserSocialForm()

    return render(request, "add-info.html", {"form": form, "type": "Add Social"})

@login_required
def update_profile_info_form(request):
    try:
        data = get_object_or_404(UserAccount, user=request.user)

        if request.method == "POST":
            data_form = UserProfileForm(request.POST, instance=data)

            if data_form.is_valid():
                data_form.save()
                messages.success(request, "Your Data updated successfully!")
                return redirect("profile")
            else:
                context = {
                    "form": data_form,
                    "type": "Update"
                }
                return render(request, "add-info.html", context=context)

        data_form = UserProfileForm(instance=data)
        context = {
            "form": data_form,
            "type": "Update"
        }
        return render(request, "add-info.html", context=context)
    except UserAccount.DoesNotExist:
        return HttpResponse("Employee Data does not exist")
    
    
@login_required
def update_social_form(request):
    try:
        data = get_object_or_404(UserSocialAccount, user=request.user)

        if request.method == "POST":
            data_form = UserSocialForm(request.POST, instance=data)

            if data_form.is_valid():
                data_form.save()
                messages.success(request, "Social Data updated successfully!")
                return redirect("profile")
            else:
                context = {
                    "form": data_form,
                    "type": "Update"
                }
                return render(request, "add-info.html", context=context)

        data_form = UserSocialForm(instance=data)
        context = {
            "form": data_form,
            "type": "Update"
        }
        return render(request, "add-info.html", context=context)
    except UserAccount.DoesNotExist:
        return HttpResponse("Social Data does not exist")
    
@login_required
def update_education_form(request):
    try:
        data = get_object_or_404(UserEducation, user=request.user)

        if request.method == "POST":
            data_form = UserEducationForm(request.POST, instance=data)

            if data_form.is_valid():
                data_form.save()
                messages.success(request, "Social Data updated successfully!")
                return redirect("profile")
            else:
                context = {
                    "form": data_form,
                    "type": "Update"
                }
                return render(request, "add-info.html", context=context)

        data_form = UserEducationForm(instance=data)
        context = {
            "form": data_form,
            "type": "Update Education"
        }
        return render(request, "add-info.html", context=context)
    except UserEducation.DoesNotExist:
        return HttpResponse("Social Data does not exist")
   
   
@login_required 
def add_position_form(request):
    if request.method == 'POST':
        form = UserJobForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect back to the original form or a success page
            return redirect('profile_info')  # Redirect back to the profile form
    else:
        form = UserJobForm()

    return render(request, 'forms/add-position.html', {'form': form})
