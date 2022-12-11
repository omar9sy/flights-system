from api.views import get_trips, AirportViewSet
from dj_rest_auth.registration.views import RegisterView
from django.urls import path
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
    PasswordResetView, UserDetailsView,
)
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('airports', get_airports),
    # path('airports/<int:pk>', get_airport),
    path('trips', get_trips),

    path('account/login/', LoginView.as_view(), name='rest_login'),
    path('account/logout/', LogoutView.as_view(), name='rest_logout'),
    path('account/user/', UserDetailsView.as_view(), name='rest_user_details'),
    # path('account/', include('dj_rest_auth.urls')),
    path('account/registration/', RegisterView.as_view(), name='rest_register'),
    # path('account/registration/', include('dj_rest_auth.registration.urls'))
]

router = DefaultRouter()
router.register(r'airports', AirportViewSet, basename='airport')
urlpatterns+=router.urls