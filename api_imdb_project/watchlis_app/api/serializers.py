from rest_framework import serializers
from watchlis_app.models import WatchList,StreamPlatform
'''
#serializers fields:handle the validation and transformation of data ex: charfield,integerfiled,FloatField
#Core Arguments for Fields:Each serializer field takes a number of common arguments ex: read_only,required etc...
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(required=True)
    age = serializers.IntegerField(required=False, default=0)
    bio = serializers.CharField(allow_blank=True, max_length=500)
    joined_at = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
'''


#Serializer   so we are commenting this next goto ModelSerializer
#Serializer: Fields must be defined manually.

'''
def desc_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Description is tooshort")

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True) #core arguments
    name=serializers.CharField()
    description=serializers.CharField(validators=[desc_length])#code arguments
    active=serializers.BooleanField()

    def create(self,validate_data): #deserilization concept comes here it will 
        return Movie.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        #here instance means stores old values and validated_data is stored new
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance
    

    #validation--------

    #1. Field level validation : it checks on a particular field. validate_(on which field apply validation)
    def validate_name(self,value):# here value holds the data of name field
        if len(value) < 2:#checks the len and send the data 
            raise serializers.ValidationError("This name is too short")
        else:
            return value
        


    #object level validation: it checks on different fields, validate(self,data):here data holds the dict type of all objects
    def validate(self,data):
        if data["name"]==data["description"]:
            raise serializers.ValidationError("name and description should be different")
        return data
    

    #validators: it perform on individual of fields with validator and a instance function. example
'''




#ModelSerializer: Fields are automatically generated based on the model.
class WatchListSerializer(serializers.ModelSerializer):
    #custom_serializer fields using serializerMethodFeild() : this will add in api this will not store in database
    # len_name=serializers.SerializerMethodField() #then create method using get_
    class Meta:
        model=WatchList
        fields="__all__" # all objects display webapi by url
        # fields=["id","name","description"]# here active is not visible in api
        # exclude=['name']# here name will not display rest is display

    # def get_len_name(self,object):
    #     length=len(object.name)
    #     return length

    # #1. Field level validation : it checks on a particular field. validate_(on which field apply validation)
    # def validate_name(self,value):# here value holds the data of name field
    #     if len(value) < 2:#checks the len and send the data 
    #         raise serializers.ValidationError("This name is too short")
    #     else:
    #         return value
        
    # #object level validation: it checks on different fields, validate(self,data):here data holds the dict type of all objects
    # def validate(self,data):
    #     if data["name"]==data["description"]:
    #         raise serializers.ValidationError("name and description should be different")
    #     return data
    


#create serializer for StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model=StreamPlatform
        fields='__all__'
