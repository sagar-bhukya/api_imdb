from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
# class Movie(models.Model):
#     name=models.CharField(max_length=50)
#     description=models.CharField(max_length=200)
#     active=models.BooleanField(default=True)

#     def __str__(self):
#         return self.name



#create StreamPlatform: for from which platform is came like prime,netflix,disney
class StreamPlatform(models.Model):
    name=models.CharField(max_length=200)
    about=models.CharField(max_length=300)
    website=models.URLField(max_length=400)
    
    def __str__(self):
        return self.name

#create watchlist different types of their like movies,tv shows,series
class WatchList(models.Model):
    title=models.CharField(max_length=200)
    storyline=models.CharField(max_length=300)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchList")#one-to-many 
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200,null=True)
    watchList=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="reviews")
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + "-" + self.watchList.title