from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("survey/", views.survey, name="survey"),
    path("foodprefer/", views.foodprefer, name="foodprefer"),
    path("itemprefer/", views.itemprefer, name="itemprefer"),
    path("upload_profile/", views.insert_profile, name="insert_profile"),
    path("upload_user/", views.insert_user, name="insert_user"),
    path("upload_food/", views.insert_food, name="insert_food"),
    path("upload_item/", views.insert_item, name="insert_item"),
]
