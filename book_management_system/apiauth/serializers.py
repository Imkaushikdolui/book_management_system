from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'pk',
            'name',
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}  # Hide password during retrieval

    def create(self, validated_data):
        password = validated_data.pop('password')
        account = Account.objects.create_user(password=password, **validated_data)
        return account


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class AccountDetailSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S%z")
    last_login = serializers.DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S%z")
    is_admin = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    class Meta:
        model = Account
        fields = [
            'name',
            'username',
            'email',
            'date_joined',
            'last_login',
            'is_admin',
            'is_active',
            'is_staff',
            'is_superuser',
        ]

