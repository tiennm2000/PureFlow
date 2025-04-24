from django.urls import path
from .controller import RegisterAPIView,LoginAPIView, LogoutAPIView, ChangePasswordAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('changepassword/', ChangePasswordAPIView.as_view(), name='changepassword'),
]
