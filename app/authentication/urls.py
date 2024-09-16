from django.urls import path, include
from .views import register_view, main_menu_view, login_view, registration_with_token_view

from .apis import (
    LoginApi,
    LogoutApi,
    RegisterApi,
    SetPasswordApi
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('main_menu/', main_menu_view, name='main_menu'),
    path('registration_with_token/', registration_with_token_view, name='registration_with_token'),
    path('login/', login_view, name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('backend_login/', LoginApi.as_view(), name='login'),
    path('logout/', LogoutApi.as_view(), name='logout'),
    path('backend_register/', RegisterApi.as_view(), name='register2'),
    path('set_password/', SetPasswordApi.as_view(), name='set_password')
]


# path(
    #     'session/',
    #     include(([
    #         path(
    #             'login/',
    #             UserSessionLoginApi.as_view(),
    #             name='login'
    #         ),
    #         path(
    #             'logout/',
    #             UserSessionLogoutApi.as_view(),
    #             name='logout'
    #         )

    #     ], "session"))
    # ),
    # path(
    #     'jwt/',
    #     include(([
    #         path(
    #             "login/",
    #             UserJwtLoginApi.as_view(),
    #             name="login"
    #         ),
    #         path(
    #             "logout/",
    #             UserJwtLogoutApi.as_view(),
    #             name="logout"
    #         )
    #     ], "jwt"))
    # ),
    # path(
    #     'me/',
    #     UserMeApi.as_view(),
    #     name='me'
    # ),