from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from .views import *
urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('routine-orders/', RoutineOrderViewSet.as_view(), name='routine_orders'),
    path('duty-rosters/', DutyRosterViewSet.as_view(), name='duty_rosters'),
    path('messages/', MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='messages'),
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/user-profile/', UserProfileView.as_view(), name='user_profile'),
]