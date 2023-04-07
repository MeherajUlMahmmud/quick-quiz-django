from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from account_control.models import UserModel


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = UserModel
        fields = [
            'username',
            'password',
        ]

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise AuthenticationFailed('Invalid credentials, try again')
            if not user.is_active:
                raise AuthenticationFailed('Account disabled, contact admin')

            return {
                'user': user,
            }
        else:
            raise serializers.ValidationError(
                "Username and password are required"
            )


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class ChangePasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()

    class Meta:
        fields = [
            'username',
            'old_password',
            'new_password',
            'confirm_password',
        ]

    def validate(self, attrs):
        username = attrs.get('username', '')
        old_password = attrs.get('old_password', '')
        new_password = attrs.get('new_password', '')
        confirm_password = attrs.get('confirm_password', '')
        if not UserModel.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                "Username does not exist"
            )
        if not authenticate(username=username, password=old_password):
            raise serializers.ValidationError(
                "Old password is incorrect"
            )
        if new_password != confirm_password:
            raise serializers.ValidationError(
                "Password does not match"
            )
        return attrs

    def save(self, **kwargs):
        username = self.validated_data['username']
        new_password = self.validated_data['new_password']
        user = UserModel.objects.get(username=username)
        user.password_plain = new_password
        user.set_password(new_password)
        user.save()
        return user


class ResetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()

    class Meta:
        fields = [
            'username',
            'new_password',
            'confirm_password',
        ]

    def validate(self, attrs):
        username = attrs.get('username', '')
        new_password = attrs.get('new_password', '')
        confirm_password = attrs.get('confirm_password', '')
        if not UserModel.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                "Username does not exist"
            )
        if new_password != confirm_password:
            raise serializers.ValidationError(
                "Password does not match"
            )
        return attrs

    def save(self, **kwargs):
        username = self.validated_data['username']
        new_password = self.validated_data['new_password']
        user = UserModel.objects.get(username=username)
        user.password_plain = new_password
        user.set_password(new_password)
        user.save()
        return user
