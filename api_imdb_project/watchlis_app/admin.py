from django.contrib import admin
from watchlis_app.models import WatchList,StreamPlatform,Review
# Register your models here.

admin.site.register([WatchList,StreamPlatform,Review])