from django.urls import path, include

urlpatterns = [
    path(
        'auth/', include(('app.authentication.urls', 'authentication'))
    ),
    path('accounts/', include(('app.users.urls', 'users'))),
    path('errors/', include(('app.errors.urls', 'errors'))),
    path('game/', include(('app.game.urls', 'game'))),
]
