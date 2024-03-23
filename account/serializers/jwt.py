from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ..exceptions import UserNotActive, UserNotFound, UserCredentialsError
from ..models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        phone_number, password = attrs['phone_number'], attrs['password']

        user = User.objects.filter(phone_number=phone_number).first()

        if user is not None:
            if not user.is_active:
                raise UserNotActive

            try:
                return super().validate(attrs)
            except AuthenticationFailed:
                raise UserCredentialsError
        else:
            raise UserNotFound