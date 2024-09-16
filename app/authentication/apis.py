from subprocess import check_output
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.forms import CharField
from app.api.mixins import ApiAuthMixin
from app.authentication.services import auth_logout, UserService
from rest_framework import serializers, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from app.users.models import Account
from app.common.utils import inline_serializer
from rest_framework_simplejwt.tokens import RefreshToken
from app.users.sql.queries.get_user import UserMeQuery, AccountDetailsQuery


class RegisterApi(APIView):
    """
    Register User
    """

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=80)
        email = serializers.EmailField()

    def post(self, request, *args, **kwargs):
        res = UserService(
            request.data,
            self.InputSerializer
        ).register_user()
        return Response(res)



class LoginApi(ObtainAuthToken):
    """
    API for login
    """
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        email = serializers.EmailField()
        name = serializers.CharField()

    def post(self, request, *args, **kwargs):

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)



        request.data['username'] = request.data['email']
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']


        refresh = RefreshToken.for_user(user)
        print(refresh)


        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


        res = AccountDetailsQuery(pk=user.id, user=user, output_check_serializer=self.OutputSerializer).get_response(token=token)

        return Response(res)


class LogoutApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        # return Response(200)
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SetPasswordApi(APIView):
    permission_classes = ()

    class InputSerializer(serializers.Serializer):
        password_1 = serializers.CharField()
        password_2 = serializers.CharField()
        token = serializers.UUIDField()

    def post(self, request, *args, **kwargs):
        user = UserService(
            request.data,
            self.InputSerializer
        ).set_password()

        if isinstance(user, Account):
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(token)

        else:
            return Response(user, status=status.HTTP_400_BAD_REQUEST)
