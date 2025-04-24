from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class AccountService:
    @staticmethod
    def register(username, first_name, last_name, email, password, phone, role='Customer', **extra_fields):
        user = User(username=username, first_name=first_name, last_name=last_name, email=email, phone=phone, role=role, **extra_fields)
        user.set_password(password)  
        user.save()
        return user

    @staticmethod
    def login(username: str, password: str):
        user = authenticate(username=username, password=password)
        if not user:
            return None
        refresh = RefreshToken.for_user(user)
        refresh['username'] = user.username
        refresh['role'] = user.role
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    @staticmethod
    def logout(refresh_token: str) -> None:
        token = RefreshToken(refresh_token)
        token.blacklist()



