from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('education', views.education, name='education'),
    path('experience', views.experience, name='experience'),
    path('skill', views.skill, name='skill'),
    path('eduDelete/<int:x>', views.edu_dlt, name='edu_dlt'),  # delete the data from experience table
    path('skillDelete/<int:x>', views.skill_dlt, name='skill_dlt'),  # delete the data from experience table
    path('expDelete/<int:x>', views.experience_dlt, name='experience_dlt'),  # delete the data from experience table

]
