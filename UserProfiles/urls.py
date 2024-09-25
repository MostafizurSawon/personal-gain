from django.urls import path
from .views import UserRegistrationView, UserLoginView, user_logout, MyProfile, add_profile_info_form, update_profile_info_form, add_position_form, add_social_form, update_social_form, update_education_form
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', MyProfile, name='profile'),
    path('profile/add-info/', update_profile_info_form, name='profile_info'),
    path('profile/add-position/', add_position_form, name='add_position'),
    path('profile/add-social/', add_social_form, name='add_social'),
    path('profile/update-social/', update_social_form, name='update_social'),
    path('profile/update-education/', update_education_form, name='update_education'),
    # path('profile/add-info/', add_profile_info_form, name='profile_info'),
]