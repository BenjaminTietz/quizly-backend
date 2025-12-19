from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed


def refresh_access_token(refresh_token_str: str) -> str:
    """
    Validate refresh token and return a new access token.
    """
    try:
        refresh_token = RefreshToken(refresh_token_str)
    except Exception:
        raise AuthenticationFailed("Invalid refresh token")

    if refresh_token.blacklisted:
        raise AuthenticationFailed("Token is blacklisted")

    return str(refresh_token.access_token)
