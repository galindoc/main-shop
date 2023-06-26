from datetime import datetime, timedelta

import jwt
from rest_framework import views, status
from rest_framework.response import Response
from django.conf import settings

from src.apps.users.serializers import UserAccountLoginSerializer, UserAccountSignupSerializer
from src.apps.users.producer import publish
from src.apps.users.utils import send_verification_email
from src.apps.users.models import UserAccount


class VerifyAccountAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        token = kwargs.get('token')
        print(token)
        if token:
            try:
                user = UserAccount.objects.get(verification_token=token)
                user.is_verified = True
                user.verification_token = ''
                user.save()
                return Response({'message': 'Account verified successfully'}, status=status.HTTP_200_OK)
            except UserAccount.DoesNotExist:
                return Response({'message': 'Invalid verification token'}, status=status.HTTP_400_BAD_REQUEST)


class UserAccountCreateAPIView(views.APIView):
    """
    Create a new user account.
    """
    def post(self, request, *args, **kwargs):
        serializer = UserAccountSignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            message_data = self._set_message_data(user, request)
            publish('user_account_created', message_data)
            send_verification_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @staticmethod
    def _set_message_data(user, request):
        return {
            'id': str(user.id),
            'name': user.name,
            'email': user.email,
            'slug': user.slug,
            'username': user.username,
            'create_default_shop': request.data.get('create_default_shop', False),
        }
    

class UserAccountLoginView(views.APIView):
    """
    Login a user account.
    """
    def post(self, request, *args, **kwargs):
        serializer = UserAccountLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            token = self._generate_token(user)
            return Response({'token': token}, status=status.HTTP_200_OK)

    @staticmethod
    def _generate_token(user):
        payload = {
            'user_id': str(user.id),
            'exp': datetime.utcnow() + timedelta(days=7),
            'iat': datetime.utcnow()
        }
        return jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')
    