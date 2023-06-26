from rest_framework import serializers
from django.db.models import Q

from src.apps.users.models import UserAccount
from src.apps.users.utils import create_username, create_verification_token

class UserAccountSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAccount
        fields = ['id', 'name', 'email', 'password', 'slug', 'username']
        read_only_fields = ['id', 'slug', 'username']

    def validate(self, attrs):
        attrs['username'] = create_username(attrs.get('name'))
        attrs['verification_token'] = create_verification_token()
        
        if not attrs.get('name'):
            raise serializers.ValidationError("Name is required")
        elif not attrs.get('email'):
            raise serializers.ValidationError("Email is required")
        elif not attrs.get('password'):
            raise serializers.ValidationError("Password is required")
        
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserAccount(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class UserAccountLoginSerializer(serializers.Serializer):
    identifier = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    def validate(self, attrs):
        if not attrs.get('identifier'):
            raise serializers.ValidationError("Email or Username is required")
        password = attrs.get('password')
        identifier = attrs.get('identifier')
        if identifier and password:
            return self._validate_credentials(identifier, password)
        
    @staticmethod
    def _validate_credentials(identifier, password):
        try:
            user = UserAccount.objects.get(
                Q(email=identifier) | Q(username=identifier)
            )
            if user.check_password(password):
                return user
            else:
                raise serializers.ValidationError("Incorrect password")
        except UserAccount.DoesNotExist:
            raise serializers.ValidationError("Incorrect email, User does not exist")
