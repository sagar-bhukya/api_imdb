from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterTestcases(APITestCase):
    def test_register(self):  # the methods should start with test name if not that method will not called at time of test cases
        #inside this we need to test everything
        # i need to get data, send post request,get response and check if the response is correct or  not. 
        # if the response is not correct thrown an error


        #1.get data in the form of json
        # while writing these test cases or whenever we are going to execute this test case, we are not going utilize our database while running the test case.
        # while running the test case django will temporarily create a new database and it will run all test cases inside the database.
        # our databse will not be effected
        data={
            "username": "testcase",
            "email":"testcase@exxample.com",
            "password":"NewPassword@123",
            "password2":"NewPassword@123"
        }
        #so data is ready then we go send post request using client 
        response=self.client.post(reverse('register'),data) # it takes two arguements 1.url endpoint 2.data.  this will give some response so store in response
        self.assertEqual(response.status_code,status.HTTP_201_CREATED) # it checks both response is okay or not


#for running test case :python manage.py test user_app


class LoginLogoutTestCases(APITestCase):
    #before performing login and logout should have to this 
    def setUp(self):
        self.user=User.objects.create_user(username="example",password="NewPassword@123")

    def test_login(self):
        data={
            "username":"example",
            "password":"NewPassword@123"
        }
        response=self.client.post(reverse('login'),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_logout(self):
        self.token=Token.objects.get(user__username="example") # once get the token, need to pass this to get credentials
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key) # so we are logged in
        response=self.client.post(reverse('logout')) #send request to logout link then which type of status code does it 
        self.assertEqual(response.status_code,status.HTTP_200_OK)

