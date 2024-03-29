from rest_framework import serializers
from .models import Blog, Category
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Blog
        fields = "__all__"

    def create(self, validated_data):
        categories = validated_data.pop('categories', [])
        blog = Blog.objects.create(**validated_data)
        for category in categories:
            blog.categories.add(category)
        return blog

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {'data': [data]}




User = get_user_model()

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not value.endswith('@redberry.ge'):
            raise serializers.ValidationError('Must use a Redberry email address.')
        return value

    def validate(self, data):
        email = data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('User with this email does not exist.')

        if not user.is_active:
            raise serializers.ValidationError('User account is disabled.')

        token, _ = Token.objects.get_or_create(user=user)
        data['token'] = token.key
        return data


