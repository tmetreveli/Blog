from django.urls import path
from .views import BlogListCreate, BlogDetail, CategoryList
from .views import login_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

urlpatterns = [
    path('blogs/', BlogListCreate.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('login/', login_view, name='login'),
]


schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="API for Blog",
   ),
   public=True,
   permission_classes=(AllowAny,),
)


urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]