from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    
    # account register endpoint
    path('register/',account_register_view,name='account-register'),    
    #simplejwt endpoints
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # account jwt and login endpoint
    path('login/',account_login_view,name='account-login'),
    path('userjwt/',user_jwt_view,name='user-jwt'),
    path('logout/',account_logout_view,name='account-logout'),
    

    # account endpoints
    path('accounts/', account_list_view, name='account-list'),
    path('account/<int:pk>/', account_detail_view, name='account-detail'),
    path('account/<int:pk>/update/', account_update_view, name='account-update'),
    path('account/<int:pk>/delete/', account_destroy_view, name='account-delete'),
    
    
    
]
