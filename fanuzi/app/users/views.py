from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status

from .models import User
from .serializers import RegisterSerializer


@permission_classes([AllowAny,])
class RegistrationUserView(CreateAPIView):
    serializer_class = RegisterSerializer
    model = User

    def post(self, request, *args, **kwargs):
        response = request.data
        if response['email']:
            serializer = self.serializer_class(data=response)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            if not serializer.is_valid(raise_exception=True):
                return Response(status=status.HTTP_401_UNAUTHORIZED)

            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)