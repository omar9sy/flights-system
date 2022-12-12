from api.views import book_seat, AirportViewSet, create_trip, get_trip
from api.views.CommentView import get_comments
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import (
    LoginView, LogoutView, UserDetailsView,
)
from django.urls import path
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('airports', get_airports),
    # path('airports/<int:pk>', get_airport),
    path('trips', create_trip),
    path('trips/<int:pk>', get_trip),
    path('trips/<int:pk>/book/<int:seat_id>', book_seat),
    path('comments', get_comments),
    path('account/login/', LoginView.as_view(), name='rest_login'),
    path('account/logout/', LogoutView.as_view(), name='rest_logout'),
    path('account/user/', UserDetailsView.as_view(), name='rest_user_details'),
    # path('account/', include('dj_rest_auth.urls')),
    path('account/registration/', RegisterView.as_view(), name='rest_register'),
    # path('account/registration/', include('dj_rest_auth.registration.urls'))
]

router = DefaultRouter()
router.register(r'airports', AirportViewSet, basename='airport')
urlpatterns += router.urls
