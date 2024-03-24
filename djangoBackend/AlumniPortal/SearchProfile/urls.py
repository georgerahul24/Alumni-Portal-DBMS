from .views import SearchProfileView
from django.urls import path

urlpatterns = [
    path('<int:rollNumber>', SearchProfileView.as_view(),name="search_profile"),

]
