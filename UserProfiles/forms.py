from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccount, JobName, UserSocialAccount, UserEducation
from django import forms

class UserRegistrationForm(UserCreationForm):
    usable_password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     if commit is True:
    #         user.save()
    #         UserAccount.objects.create(
    #             user = user,
    #         )
    #     return user
    
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        # fields = '__all__'
        fields = ['image','gender','hometown','country','mobile', 'age', 'job', 'position','address', 'description', 'company'] 
        
        labels = {
            'gender': 'Gender',
            'hometown': 'Hometown',
            'address': 'Address',
            'mobile': 'Mobile Number',
            'age': 'Age',
            'description': 'Short Description',
            'country': 'Country',
            'job': 'Current Status',
            'position': 'Job Position',
            'company': 'Company Name',
        }
        
class UserEducationForm(forms.ModelForm):
    class Meta:
        model = UserEducation
        # fields = '__all__'
        # fields = ['image','gender','hometown','country','mobile', 'age', 'job', 'position','address', 'description'] 
        exclude = ['user']
        
        labels = {
            'last_education': 'Last education',
            'subject': 'Subject',
            'year': 'Passing Year',
            'result': 'Result',
            'background': 'Your Background',
            'ssc_school': 'SSC School',
            'ssc_subject': 'SSC Group',
            'ssc_year': 'SSC completed year',
            'hsc_school': 'HSC College',
            'hsc_subject': 'HSC Group',
            'hsc_year': 'HSC completed year',
            'university': 'University',
            'university_year': 'University completed year',
            'bootcamp': 'Bootcamp name (If completed any)',
        }
    
    
    
class UserJobForm(forms.ModelForm):
    class Meta:
        model = JobName
        fields = '__all__'
        # fields = ['gender','hometown','address','mobile', 'age'] 
        
class UserSocialForm(forms.ModelForm):
    class Meta:
        model = UserSocialAccount
        # fields = '__all__'
        exclude= ['user']
        

        