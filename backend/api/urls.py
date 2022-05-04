from api import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
