from rest_framework import serializers

from src.apps.sections.models import ContentImage


class ContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentImage
        fields = '__all__'
        read_only_fields = ('id',)
