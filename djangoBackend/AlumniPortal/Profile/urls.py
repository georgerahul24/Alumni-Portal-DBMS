from .views import YourProfileView
from django.urls import path

urlpatterns = [
    path('', YourProfileView.as_view()),
    path('yourProfile', YourProfileView.as_view(), name='yourProfile'),

]
