from django.contrib.auth.models import User

from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    #read only means:user cannot update it, but can read it,can access it
    #write only:user can send information about password but cannot read it
    password2=serializers.CharField(style={'input_type':'password'},write_only=True) #we can see in adminpanel user password
                                    #whenever some is entering some data,we can use input type as password 
    class Meta:
        model=User# by default django has username, email,password fields only
        fields=['username','email','password','password2']# am going add password2 for a confirmation
        extra_kwargs={
            'password':{'write_only':True}# we set here write only for password also
        }

    def save(self):
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password !=password2:
            raise serializers.ValidationError({'error':'p1 and p2 should be same!'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():# checks for unique email
            raise serializers.ValidationError({'error':'Email already Exists'})
        
        account=User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account        
    