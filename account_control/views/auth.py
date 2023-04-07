from rest_framework import views, generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from account_control.serializers.auth import (LoginSerializer, LogoutSerializer, ResetPasswordSerializer,
                                              ChangePasswordSerializer)
from account_control.serializers.user import UserModelSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = UserModelSerializer.Write
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserModelSerializer.List(user).data
        tokens = get_tokens_for_user(user)
        return Response({'data': user_data, "tokens": tokens, }, status=HTTP_200_OK)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user:
            user_data = UserModelSerializer.List(user).data
            tokens = get_tokens_for_user(user)
            return Response({'user': user_data, "tokens": tokens, }, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LogoutAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data['refresh_token']
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'detail': str(e)}, status=HTTP_400_BAD_REQUEST)


class ChangePasswordAPIView(views.APIView):
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Password changed successfully'}, status=HTTP_200_OK)


class ResetPasswordAPIView(APIView):
    http_method_names = ['post']
    permission_classes = [IsAdminUser]
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Password reset successful'}, status=HTTP_200_OK)
