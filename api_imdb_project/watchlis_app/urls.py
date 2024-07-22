from django.urls import path
from .views import movie_list,movies_details
urlpatterns = [
    path('list/',movie_list,name="movie-list"),
    path('list/<int:pk>',movies_details,name="movie-datails"),
]
