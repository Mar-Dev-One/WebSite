# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # User authentication
    path('register/', views.UserRegistrationView.as_view(), name='user_register'),
    path('profile/', views.get_user_profile, name='user_profile'),
    path('profile/update/', views.update_user_profile, name='update_profile'),
    path('profile/upload-picture/', views.upload_profile_picture, name='upload_profile_picture'),
    
    # Protected endpoints
    path('protected/', views.protected_view, name='protected'),
    path('admin-only/', views.admin_only_view, name='admin_only'),
    path('verified-only/', views.verified_users_only_view, name='verified_only'),
    
    # Add your other API endpoints here
]