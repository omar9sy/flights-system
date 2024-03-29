from api.views import (
    book_seat, AirportViewSet, create_trip, search_trip, get_airport_trips,
    get_user_trips, get_airport_trip_reservations, UserDetailsView2,
    add_email, AirportRegisterView, LoginViewWithRole, TripViewSet, get_hotels_and_restaurants)
from api.views.AdminView import update_balance, get_users
from api.views.CommentView import get_comments
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import (
    LogoutView, PasswordChangeView,
)
from django.urls import path
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('airports', get_airports),
    # path('airports/<int:pk>', get_airport),
    path('trips', create_trip),
    path('trips/my', get_user_trips),
    path('trips/<int:pk>/reservations', get_airport_trip_reservations),
    path('trips/<int:pk>/book/<int:seat_id>', book_seat),
    path('trips/search',search_trip),
    path('comments', get_comments),
    path('airports/me',get_airport_trips),
    path('airports/emails', add_email),
    path('airports/register', AirportRegisterView.as_view()),
    path('hotels_and_restaurants', get_hotels_and_restaurants),
    # path('airports/my_reservations', AirportRegisterView.as_view()),
    path('users/balance', update_balance),
    path('users', get_users),
    path('account/login/', LoginViewWithRole.as_view(), name='rest_login'),
    path('account/logout/', LogoutView.as_view(), name='rest_logout'),
    path('account/user/', UserDetailsView2.as_view(), name='rest_user_details'),
    path('account/user/change-password', PasswordChangeView.as_view(), name='rest_change_reset'),
    # path('account/', include('dj_rest_auth.urls')),
    path('account/registration/', RegisterView.as_view(), name='rest_register'),
    # path('account/registration/', include('dj_rest_auth.registration.urls'))
]

router = DefaultRouter()
router.register(r'airports', AirportViewSet, basename='airport')
router.register(r'trips', TripViewSet, basename='trip')
urlpatterns += router.urls
