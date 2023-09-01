from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)
    college_name=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff', 'is_authenticated', 'address', 'phone_number','college_name')

    def create(self, validated_data):
        password = validated_data.pop('password')
        phone_number = validated_data.pop('phone_number')
        address = validated_data.pop('address')
        collge_name=validated_data.pop('college_name')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        user.address = address
        user.phone_number = phone_number
        user.college_name=collge_name
        user.save()

        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        ordering = ('username',)
