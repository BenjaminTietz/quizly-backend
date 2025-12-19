from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    confirmed_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'confirmed_password']
        extra_kwargs = {
            'password': {'write_only': True}    
        }
        
    def create(self, validated_data):
        validated_data.pop('confirmed_password', None)
        user = User.objects.create_user(**validated_data)
        return user
    



class RefreshTokenSerializer(serializers.Serializer):
    """
    Serializer to extract refresh token from HTTP-only cookies.
    """

    def validate(self, attrs):
        request = self.context.get("request")
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            raise AuthenticationFailed("Refresh token missing")

        attrs["refresh_token"] = refresh_token
        return attrs
