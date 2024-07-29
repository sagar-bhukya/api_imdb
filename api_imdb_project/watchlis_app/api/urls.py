from django.urls import path
# from watchlis_app.api.views import movie_list,movies_details
from watchlis_app.api.views import MovieListAv,MovieDetailAV,StreamPlatformAv,StreamPlatformDetailAV
urlpatterns = [
    path('list/',MovieListAv.as_view(),name="movie-list"),
    path('list/<int:pk>/',MovieDetailAV.as_view(),name="movie-datails"),
    path('stream/',StreamPlatformAv.as_view(),name="stream"),
    path('stream/<int:id>/',StreamPlatformDetailAV.as_view(),name="stream-detail"),
]
