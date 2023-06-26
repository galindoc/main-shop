from rest_framework import serializers

from src.apps.sections.models import Content
from src.apps.sections.serializers import ContentTextSerializer, ContentImageSerializer


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
        read_only_fields = ('id',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.text:
            data['text'] = ContentTextSerializer(instance.text).data
        if instance.image:
            data['image'] = ContentImageSerializer(instance.image).data
        return data
