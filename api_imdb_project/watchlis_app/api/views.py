from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from watchlis_app.models import WatchList,StreamPlatform,Review
from .serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.decorators import api_view #function based views
from rest_framework import status
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics
#filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

#pagination
from watchlis_app.api.pagination import MoviewlistPagination,MoviewlistLOPagination,MoviewlistCursorPagination


from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle #local throttling

from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from rest_framework.views import APIView #class based views

from watchlis_app.api.permissions import IsAdminOrReadOnly,IsReviewUserOrReadOnly

from watchlis_app.api.throttling import ReviewCreateThrottle,ReviewListThrottle

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
    permission_classes = [IsAdminOrReadOnly] #only admin can edit rest of all them read only
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

    permission_classes = [IsAdminOrReadOnly] #only admin can edit rest of all them read only

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
    


class Moviewlist(generics.ListAPIView):
    queryset=WatchList.objects.all()
    serializer_class = WatchListSerializer

    # pagination_class=MoviewlistPagination  #PageNumberPagination
    # pagination_class=MoviewlistLOPagination  #LimitOffsetPagination

    pagination_class=MoviewlistCursorPagination #CursorPagination

    # #django-filertBackend used to filter something like amozon website
    # filter_backends = [DjangoFilterBackend] #used on only generic views mostly ListAPIView
    # filterset_fields=['title','platform__name']

    #SearchFilter: when the user give some input that we need to find and give him back to display
    # filter_backends=[filters.SearchFilter]
    # search_fields=['^title','platform__name'] #localhost:8000/watch/list2/?search=The
    '''

Prefix	Lookup	
^	istartswith	Starts-with search.
=	iexact	Exact matches.
$	iregex	Regex search.
@	search	Full-text search (Currently only supported Django's PostgreSQL backend).
None	icontains	Contains search (Default).

    '''

    #OrderingFilter
    filter_backends=[filters.OrderingFilter]#localhost:8000/watch/list2/?ordering=avg_arting  asc to desc
                                            #localhost:8000/watch/list2/?ordering=-avg_arting  desc to asc
    ordering_fields=['avg_arting']

    









'''
#viewsets-------------allows you to combine the logic for a set of related views in a single class
#A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create().

class StreamPlatformViewset(viewsets.ViewSet):
    def list(self,request):
        queryset=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        queryset=StreamPlatform.objects.all()
        watchList=get_object_or_404(queryset,pk=pk)
        serializer=StreamPlatformSerializer(watchList)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def update(self,request,pk=None):
        queryset= StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk=None):
        queryset=StreamPlatform.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

#modelViewSet : it provides by default actions `create()`, `retrieve()`, `update()`,`partial_update()`, `destroy()` and `list()` actions.    
# wheneven you hit the api that will give you only GET, POST, if you access By id that will give  GET, PUT, PATCH, DELETE
class StreamPlatformViewset(viewsets.ModelViewSet): # and another one is ReadOnlyModelViewset it gives only Retrive and list
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer #serializer_class must give
    permission_classes = [IsAdminOrReadOnly] #only admin can edit rest of all them read only




class StreamPlatformAv(APIView):
    permission_classes = [IsAdminOrReadOnly] #only admin can edit rest of all them read only
    def get(self,request):
        platform=StreamPlatform.objects.all()
        # serializer=StreamPlatformSerializer(platform,many=True,context={'request': request})# context used when it comes to hyperlink
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
    permission_classes = [IsAdminOrReadOnly] #only admin can edit rest of all them read only
    def get(self,request,id):
        try:
            platform=StreamPlatform.objects.get(id=id)
        except StreamPlatform.DoesNotExist:
            return Response({'message':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
    
        serializer=StreamPlatformSerializer(platform)
        return Response(serializer.data)
    

    def put(self,request,id):
        platform=StreamPlatform.objects.get(id=id)
        serializer=StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        platform=StreamPlatform.objects.get(id=id)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




#mixins-------esily cna do  create/retrieve/update/delete
#1.ListModelMixin : list(request,*args,**kwargs)
#2.CreateModelMixin : create()
#3.RetrieveModelMixin:retrive()
#4.UpdateModelMixin : update()
#5.DestroyModelMixin:destroy()
from rest_framework import generics,mixins

# class ReviewMixins(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     #generic views attributes 
#     queryset=Review.objects.all() #
#     serializer_class=ReviewSerializer #used for validating and deserializing input, and for serializing output.

#     def get(self,request,*args, **kwargs): #get all in list
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):#create review
#         return self.create(request,*args,**kwargs)


# class ReviewMixinsDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)#retrive
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)





class UserReview(generics.ListAPIView):
    serializer_class=ReviewSerializer
    
    #write get_query for filtering
    # def get_queryset(self):
    #     username=self.kwargs['username']
    #     return Review.objects.filter(review_user__username=username) # thise __ gives for only this if you want filter about rating just give one _
    

    def get_queryset(self):
        username = self.request.query_params.get('username',None) #it takes after watch/reviews/?username=sagar
        return Review.objects.filter(review_user__username=username) # thise __ gives for only this if you want filter about rating just give one _
    

#generic views as we write mixins code now this will not write any methods

class ReviewMixins(generics.ListAPIView):
    serializer_class = ReviewSerializer
    #block level permission it use for only this one
    permission_classes=[IsAuthenticated]   # when i access this without logged in this will give me->"detail": "Authentication credentials were not provided."
    
    throttle_classes=[ReviewListThrottle,AnonRateThrottle] #for local

    filter_backends = [DjangoFilterBackend] #used on only generic views mostly ListAPIView
    filterset_fields=['review_user__username','active']

    def get_queryset(self):
        pk = self.kwargs['pk']  # Access the 'pk' parameter from the URL
        return Review.objects.filter(watchList=pk)  # Filter reviews by the 'watchList' ID
    
class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]

    throttle_classes=[ReviewCreateThrottle] # throttling scope get

    def perform_create(self,serializer): #it will act as post 
        pk=self.kwargs.get('pk')
        watchList=WatchList.objects.get(pk=pk)#here what pk we are giving that will act as foreign key
        review_user=self.request.user #access the user 
        review_queryset=Review.objects.filter(watchList=watchList,review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie ")
        
        if watchList.number_rating==0:
            watchList.avg_arting=serializer.validated_data['rating'] #getting new rating value
        else:
            watchList.avg_arting=(watchList.avg_arting + serializer.validated_data['rating'])/2
        
        watchList.number_rating=watchList.number_rating+1
        watchList.save()

        serializer.save(watchList=watchList,review_user=review_user)

class ReviewMixinsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    throttle_classes=[ScopedRateThrottle] #this for without creating any file for separate
    throttle_scope='review-detail' # give how many requests do they want to send
    # permission_classes=[IsAuthenticatedOrReadOnly]# we can read only if user is not logged in

    # permission_classes=[IsAdminOrReadOnly]# here when the user logged then only can see the delete and edit option either he can see only get method
    permission_classes=[IsReviewUserOrReadOnly]# only admin can edit rest of all onlg get