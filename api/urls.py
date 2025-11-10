from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.test_views import Test, TestAuthentication
from .views.register_user import RegisterView

urlpatterns = [
    path('test/', Test.as_view(), name='test'),
    path('test_autentication/', TestAuthentication.as_view(), name='test_autentication'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterView.as_view(), name='register'),
]