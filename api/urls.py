from django.urls import path, include

urlpatterns = [
    path('account/', include('dj_rest_auth.urls')),
    path('account/registration/', include('dj_rest_auth.registration.urls'))
]
