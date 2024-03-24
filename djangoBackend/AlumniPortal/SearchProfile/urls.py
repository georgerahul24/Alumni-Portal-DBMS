from .views import SearchProfileView, SearchBarView,SearchResultsView
from django.urls import path

urlpatterns = [
    path('<int:rollNumber>', SearchProfileView.as_view(), name="search_profile"),
    path('searchbar/', SearchResultsView.as_view(), name="search_results"),
    path('', SearchBarView.as_view(), name="searchbar"),

]
