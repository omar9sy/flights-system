from api.views import get_airports, get_trips
from dj_rest_auth.registration.views import RegisterView
from django.urls import path
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
    PasswordResetView, UserDetailsView,
)

urlpatterns = [
    path('airports', get_airports),
    path('trips', get_trips),

    path('account/login/', LoginView.as_view(), name='rest_login'),
    path('account/logout/', LogoutView.as_view(), name='rest_logout'),
    path('account/user/', UserDetailsView.as_view(), name='rest_user_details'),
    # path('account/', include('dj_rest_auth.urls')),
    path('account/registration/', RegisterView.as_view(), name='rest_register'),
    # path('account/registration/', include('dj_rest_auth.registration.urls'))
]
