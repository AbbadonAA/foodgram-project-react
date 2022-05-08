# from api import views
from django.urls import include, path
# from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet

app_name = 'api'
router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
