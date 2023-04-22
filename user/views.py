from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from .serializers import AuthUserSerializer, UserRestaurantRelationSerializer
from .models import User, UserRestaurantRelation


class RegisterUserView(CreateAPIView):
    """Registrate a new user"""
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer
    permission_classes = (AllowAny,)


class LogoutView(APIView):
    """Logout user"""

    def post(self, request):
        try:
            refresh_token = request.data
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserRestaurantRelationView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserRestaurantRelation.objects.all()
    serializer_class = UserRestaurantRelationSerializer
    lookup_field = 'restaurant'

    def get_object(self):
        obj, _ = UserRestaurantRelation.objects.get_or_create(
            User=self.request.user,
            resaurant_id=self.kwargs['restaurant'])
        return obj
