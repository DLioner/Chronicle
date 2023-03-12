from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from user.serializer import (PasswordChangeSerializer, RegistrationSerializer,
                             UserSerializer)

from redis_helper import redis_instance
User = get_user_model()

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_password(request):
    try:
        data = {}
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data["message"] = f"user successfully changed password"
        else:
            data = serializer.errors
    except KeyError as e:
        raise ValidationError(f'Field {str(e)} is missing')


class UsersListAPIView(APIView):
    def get(self, request):
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ('__all__')
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        users = User.objects.filter(is_deleted=False)
        serializer = UserSerializer(users, many=True)
    
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    authentication_classes = (JWTTokenUserAuthentication, )
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        data = []
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data["message"] = "user registered successfully"
            data["email"] = user.email
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.is_deleted = True
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return get_user_model().objects.get(pk=pk, is_deleted=False)
        except get_user_model().DoesNotExist:
            raise Response('Data not found', status=status.HTTP_404_NOT_FOUND)