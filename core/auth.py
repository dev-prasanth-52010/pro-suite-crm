# core/auth.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("access")
        print("cookie token", token)
        
        if not token:
            return None
        
        try:
            # Validate token directly (correct way)
            validated_token = self.get_validated_token(token)
            user = self.get_user(validated_token)
            return (user, validated_token)
        except (InvalidToken, TokenError):
            print("Invalid token")
            return None
