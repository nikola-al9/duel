from django.urls import path, include
from rest_framework import routers

from .apis import *

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # path('', UserListApi.as_view(), name='list'),
    path('me/', UserMeApi.as_view(), name='userMe'),
    path('account/', AccountApi.as_view(), name='account'),
]
