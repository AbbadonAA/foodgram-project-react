from djoser.views import UserViewSet

from .models import User

# from .serializers import CustomUserSerializer


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    # serializer_class = CustomUserSerializer
    http_method_names = ['get', 'post', 'head', 'options']
