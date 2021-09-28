from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from market import views

urlpatterns = [
    path("", views.main, name="main"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("upload_user/", views.insert_user, name="insert_user"),
    path("upload_data/", views.insert_db, name="insert_db"),
    path("similar_user/", views.similar_user, name="similar_user"),
    path("recom_user/", views.recom_user, name="recom_user"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
]
