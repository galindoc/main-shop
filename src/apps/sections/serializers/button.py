from rest_framework import serializers
from src.apps.sections.models import Button


class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = '__all__'
