from django.urls import path,include
# from watchlis_app.api.views import movie_list,movies_details
from watchlis_app.api.views import MovieListAv,MovieDetailAV,StreamPlatformAv,StreamPlatformDetailAV,ReviewMixins,ReviewMixinsDetails,ReviewCreate,UserReview,Moviewlist
from rest_framework.routers import DefaultRouter
from watchlis_app.api.views import StreamPlatformViewset


router=DefaultRouter()
router.register('stream',StreamPlatformViewset,basename='streamplatform')# we need to register with viewset from views
urlpatterns = [
    path('list/',MovieListAv.as_view(),name="movie-list"),
    path('list/<int:pk>/',MovieDetailAV.as_view(),name="movie-datails"),
    path('list2/',Moviewlist.as_view(),name="movie-datails"),
    path('',include(router.urls)), #/watch/stream here its combining the both views 
    # '''   
    # path('stream/',StreamPlatformAv.as_view(),name="stream"),
    # path('stream/<int:id>/',StreamPlatformDetailAV.as_view(),name="stream-detail"),
    # '''



    # path('reviews/',ReviewMixins.as_view(),name="reviews"),
    # path('stream/<int:pk>/reviews/',ReviewMixinsDetails.as_view(),name="review-details"),
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name="review-create"),
    path('<int:pk>/reviews/',ReviewMixins.as_view(),name="reviews-list"),
    path('review/<int:pk>/',ReviewMixinsDetails.as_view(),name="review-detail"),

    #throttling
    # path('reviews/<str:username>/',UserReview.as_view(),name="user-reviews"),

    path('reviews/',UserReview.as_view(),name="user-reviews"),

]
