"""
URL configuration for DocumentVerifierDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from .views import *
from django.urls import path

urlpatterns = [
    path('', SettingsView.as_view(), name='settings'),
    path('aboutme/', AboutMeView.as_view()),
    path('socialmedia/', SocialMediaView.as_view()),
    path('password/', PasswordView.as_view(), name='about'),
    path('profiledetails/', ProfileView.as_view(), name='socialmedia'),

    path('newEducation/', NewEducationView.as_view(), name='newEducation'),
    path('newAccomplishment/', NewAccomplishmentView.as_view(), name='newAccomplishment'),
    path('newExperience/', NewExperienceView.as_view(), name='newExperience'),

    path('editEducation/<int:educationID>', editEducationView.as_view(), name='editEducation'),
    path('editAccomplishment/<int:accomplishmentID>', editAccomplishmentsView.as_view(), name='editAccomplishment'),
    path('editExperience/<int:experienceID>', editExperienceView.as_view(), name='editExperience'),

    path('deleteEducation/<int:educationID>', deleteEducationView.as_view(), name='deleteEducation'),
    path('deleteAccomplishment/<int:accomplishmentID>', deleteAccomplishmentView.as_view(), name='deleteAccomplishment'),
    path('deleteExperience/<int:experienceID>', deleteExperienceView.as_view(), name='deleteExperience'),



]
