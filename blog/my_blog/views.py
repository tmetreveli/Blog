from rest_framework import generics, permissions
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthTokenSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token




class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        queryset = Blog.objects.all()
        categories = self.request.query_params.get('categories')
        if categories:
            category_list = categories.split(',')
            queryset = queryset.filter(categories__name__in=category_list).distinct()
        return queryset

class BlogDetail(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(['POST'])
@permission_classes([])
def custom_obtain_auth_token(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(read_only=True)

   
User = get_user_model()


@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    username = email  

    user, created = User.objects.get_or_create(username=username, defaults={'email': email})
    if created:
        user.save()

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})