from django import views
from app.common.mixins import MyDestroyModelMixin
from app.common.serializers import CheckIntPkSerializer
from app.common.services import CountConnections
from app.common.utils import get_response
from app.users import permissions
from rest_framework import mixins, serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from app.authentication.services import UserService
from .permissions import *
from .sql.queries.get_user import UserMeQuery


class UserMeApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        res = UserMeQuery(user=request.user, pk=request.user.id).get_response()
        return Response(res)


class AccountApi(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        res = UserService(
            request.data,
            user=request.user
        ).update()
        return Response(res)
