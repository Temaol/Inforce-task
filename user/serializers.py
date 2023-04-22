from rest_framework.serializers import ModelSerializer

from .models import User, UserRestaurantRelation


class AuthUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserRestaurantRelationSerializer(ModelSerializer):
    class Meta:
        model = UserRestaurantRelation
        fields = ('restaurant', 'vote')
