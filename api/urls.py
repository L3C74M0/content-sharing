from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.test_views import Test, TestAuthentication
from .views.register_user import RegisterView
from .views.media_content import MediaContentListCreate, MediaContentDetail
from .views.user_profile import UserProfileList, UserProfileDetail
from .views.rating import RatingListCreate


urlpatterns = [
    path('test/', Test.as_view(), name='test'),
    path('test_autentication/', TestAuthentication.as_view(), name='test_autentication'),

    path('register/', RegisterView.as_view(), name='register'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('media/', MediaContentListCreate.as_view(), name='media_list_create'),
    path('media/<int:pk>/', MediaContentDetail.as_view(), name='media_detail'),

    path('profiles/', UserProfileList.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='profile_detail'),

    path('ratings/', RatingListCreate.as_view(), name='rating_list_create'),
    #path('ratings/<int:pk>/', RatingDetail.as_view(), name='rating_detail'),
]