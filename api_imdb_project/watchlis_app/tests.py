from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from watchlis_app.api import serializers
from watchlis_app import models

class StreamPlatformTestCase(APITestCase):
    #create a normal user they
    def setUp(self) -> None:
        self.user=User.objects.create_user(username="example",password="NewPassword@123")
        self.token=Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

        #here manually created data
        self.stream=models.StreamPlatform.objects.create(name="netflix",about="#1 streaming platform",website="https://netflix.com")

    def test_streamplatform_create(self):# send the normal to give forbidden
        data={
            "name":"netflix",
            "about":"#1 streaming platform",
            "website":"https://netflix.com"
        }
        response=self.client.post(reverse('streamplatform-list'),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):# get all list 
        response=self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_streamplatform_indiv(self):
        response=self.client.get(reverse('streamplatform-detail',args=(self.stream.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)



class WatchListTesteCase(APITestCase):
    def setUp(self) -> None:
        self.user=User.objects.create_user(username="example",password="NewPassword@123")
        self.token=Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

        #here manually created data
        self.stream=models.StreamPlatform.objects.create(name="netflix",about="#1 streaming platform",website="https://netflix.com")
        #movie created manually
        self.watchlist=models.WatchList.objects.create(platform=self.stream,title="Example Movie",storyline="Example Story",active=True)
    def test_watchlist_create(self):
        data={
            "platform":self.stream,
            "title":"Example Movie",
            "storyline":"Example Story",
            "active":True
        }

        response=self.client.post(reverse('movie-list'),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    
    def test_watchlist_list(self):
        response=self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_watchlist_indvi(self):
        response=self.client.get(reverse('movie-datails',args=(self.watchlist.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')

    

class ReviewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user=User.objects.create_user(username="example",password="NewPassword@123")
        self.token=Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

        #here manually created data
        self.stream=models.StreamPlatform.objects.create(name="netflix",about="#1 streaming platform",website="https://netflix.com")
        #movie created manually
        self.watchlist=models.WatchList.objects.create(platform=self.stream,title="Example Movie",storyline="Example Story",active=True)

        self.watchlist2=models.WatchList.objects.create(platform=self.stream,title="Example Movie",storyline="Example Story",active=True)

        self.review=models.Review.objects.create(review_user=self.user,rating=5,description="Great Movie",watchList=self.watchlist2,active=True)

    def test_review_create(self):
        data={
            "review_user":self.user,
            "rating":5,
            "description":"Great Movie",
            "watchlist":self.watchlist,
            "active":True
        }
        response=self.client.post(reverse('review-create',args=(self.watchlist.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)
        # self.assertEqual(models.Review.objects.get().rating, 5)


        #we are not allow to user create one more review # will give use bad request 400
        response=self.client.post(reverse('review-create',args=(self.watchlist.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    
    def test_review_create_unauth(self):
        data={
            "review_user":self.user,
            "rating":5,
            "description":"Great Movie",
            "watchlist":self.watchlist,
            "active":True
        }
        self.client.force_authenticate(user=None)# gives unauthenticated user
        response=self.client.post(reverse('review-create',args=(self.watchlist.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)


    def test_review_update(self):
        data={
            "review_user":self.user,
            "rating":4,
            "description":"Great Movie---updated",
            "watchlist":self.watchlist,
            "active":False
        }
        response=self.client.put(reverse('review-detail',args=(self.review.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_review_list(self):
        response=self.client.get(reverse('reviews-list',args=(self.watchlist.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_review_indi(self):
        response=self.client.get(reverse('review-detail',args=(self.review.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

