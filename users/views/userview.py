from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.serializers import UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_serializer = self.serializer_class(data = request.data)
        user_serializer.is_valid(raise_exception = True)
        user_serializer.save()

        token_serializer = TokenObtainPairSerializer(data = {
            'username': request.data['username'],
            'password': request.data['password']
        })
        token_serializer.is_valid(raise_exception = True)
        return Response(token_serializer.validated_data, status = status.HTTP_201_CREATED)