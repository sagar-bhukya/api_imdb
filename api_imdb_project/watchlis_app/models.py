from django.db import models


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
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title