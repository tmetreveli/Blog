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
@permission_classes([])
def login_view(request):
    serializer = AuthTokenSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        user, _ = User.objects.get_or_create(email=email)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

