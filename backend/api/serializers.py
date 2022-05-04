from rest_framework.serializers import ModelSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = (
        # 'id', 'username', 'first_name',
        # 'last_name'
        # )

        fields = (
            'email', 'username', 'first_name',
            'last_name', 'password'
        )
