from rest_framework import   serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
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
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    # country = serializers.CharField()
    # address = serializers.CharField()
    # phone = serializers.CharField()
    # bio = serializers.CharField()
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "country", "address", "phone", "bio", "id" ]
        # read_only_fields = ["id", "user"]
        
    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.counrty = validated_data.get('country', instance.country)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.bio = validated_data.get('bio', instance.bio)
    #     instance.save()
    #     return instance