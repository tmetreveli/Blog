from rest_framework import serializers
from .models import Blog, Category

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'




class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(read_only=True)

    def validate_email(self, value):
        # Check if the email ends with @redberry.ge
        if not value.endswith('@redberry.ge'):
            raise serializers.ValidationError('Must use a Redberry email address.')
        return value

    def validate(self, data):
        # Validate the email is provided
        email = data.get('email')

        # Try to retrieve the user with the given email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('User with this email does not exist.')

        # Check if user is active or any other business logic
        if not user.is_active:
            raise serializers.ValidationError('User account is disabled.')

        # If user exists and is active, create or get existing token
        token, created = Token.objects.get_or_create(user=user)
        data['token'] = token.key
        return data

