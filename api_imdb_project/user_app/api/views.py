from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token

# from rest_framework_simplejwt.tokens import RefreshToken #for creating tokens manually

@api_view(['POST'])
def registration_view(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)

        data={}
        if serializer.is_valid():
            account=serializer.save()

            data['response']="Registration successfully!.."
            data['username']=account.username
            data['email']=account.email

            token=Token.objects.get(user=account).key
            data['token']=token

            
            # # here while registration it will gona create both refresh and access tokens 
            # refresh= RefreshToken.for_user(account)
            # data['token'] ={
            #     'refresh' : str(refresh),
            #     'access' : str(refresh.access_token),
            # }
        else:

            data=serializer.errors
        return Response(data,status=status.HTTP_201_CREATED)
        

#logout or delete account or destroy token
@api_view(['POST'])
def logout_view(request):

    if request.method =='POST':
        request.user.auth_token.delete()# here the get current user token and delete that
        return Response(status=status.HTTP_200_OK)

