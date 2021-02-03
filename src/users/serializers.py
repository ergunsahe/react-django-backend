from rest_framework import   serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer
from django.contrib.auth import get_user_model
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password], style={'input_type':'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type':'password'})
    
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "password2"
        )
    
    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords didn't match"})
        
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        
        return user
    

class ProfileSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "country", "address", "phone", "bio", "id" ]
        # read_only_fields = ["id", "user"]
        
    
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username')


class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')