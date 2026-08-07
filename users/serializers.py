from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()  

class RegisterSerializer(serializers.ModelSerializer): 
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta: 
        model = User
        fields = ["id", "email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        password = validated_data.pop("password") #removes  password form dictionary, and sotes its value in a seperate variable named password. 
        return User.objects.create_user(password=password, **validated_data)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]