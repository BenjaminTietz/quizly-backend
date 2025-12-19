from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


from .serializers import RefreshTokenSerializer
from .utils import refresh_access_token

# Create your views here.
class RegisterView(APIView):
    
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class RefreshTokenView(APIView):
    """
    Refresh access token using refresh token from HTTP-only cookie.
    """

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = RefreshTokenSerializer(
            data={}, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        access_token = refresh_access_token(
            serializer.validated_data["refresh_token"]
        )

        response = Response(
            {
                "detail": "Token refreshed",
                "access": access_token,
            },
            status=status.HTTP_200_OK,
        )

        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=300,
        )

        return response