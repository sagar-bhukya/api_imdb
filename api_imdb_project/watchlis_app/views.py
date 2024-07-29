# from django.shortcuts import render
# from watchlis_app.models import Movie

# from django.http import JsonResponse # need to show in the form of json

# # Create your views here.

# def movie_list(request):
#     movies=Movie.objects.all()# query set for getting all movies
#     # print(movies)# it gives in the form of list
#     data={
#         'movies_list': list(movies.values())
#     }
#     # print(list(movies.values()))# this will give us in the form of dictionary

#     return JsonResponse(data)

# # for specific id
# def movies_details(request,pk):
#     movie=Movie.objects.get(pk=pk)
#     data={
#         'name':movie.name,
#         'description':movie.description,
#         'active':movie.active
#     }
#     return JsonResponse(data)
# #the above is all are manual work




# #from now using django restframework 

