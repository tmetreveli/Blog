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
def login_view(request):
    serializer = AuthTokenSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response({'token': serializer.validated_data['token']})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)