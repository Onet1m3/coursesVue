from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ( 'first_name', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data['email']
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user