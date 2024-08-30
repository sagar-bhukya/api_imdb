from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token# this gives us access token if we send our username and password
from .views import registration_view,logout_view
urlpatterns = [
    path('login/',obtain_auth_token,name="login"),# post request then only get token 
    path('register/',registration_view,name='register'),
    path('logout/',logout_view,name="logout"),
]
