from rest_framework.response import Response
from watchlis_app.models import WatchList,StreamPlatform
from .serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework.decorators import api_view #function based views
from rest_framework import status
from django.shortcuts import render

from rest_framework.views import APIView #class based views

#function based views -----------------------

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method=='GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)# for getting more we need to give many==true
#         return Response(serializer.data)#This converts the data into a dictionary (or list of dictionaries).
#         # return render(request,'movies/movie_list.html',{'movies':serializer.data})
#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movies_details(request,pk):
#     if request.method=='GET':
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'message':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method=='PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method=='DELETE':
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






#class based views---------------------
class MovieListAv(APIView):
    def get(self,request): #here we are directly define get method and here we not gona write any if condition like function based views
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)# for getting more we need to give many==true
        return Response(serializer.data)#This converts the data into a dictionary (or list of dictionaries).
    
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class MovieDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'message':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StreamPlatformAv(APIView):
    def get(self,request):
        platform=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#for specific stream update      
class StreamPlatformDetailAV(APIView):
    
    def get(self,request,id):
        platform=StreamPlatform.objects.get(id=id)
        serializer=StreamPlatformSerializer(platform)
        return Response(serializer.data)
    

    def put(self,request,id):
        platform=StreamPlatform.objects.get(id=id)
        serializer=StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,id):
        platform=StreamPlatform.objects.get(id=id)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)