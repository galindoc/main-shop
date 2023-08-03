from rest_framework import serializers

from src.apps.sections.models import Section
from src.apps.sections.serializers import SingleImageContentSerializer, DoubleImageContentSerializer


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        read_only_fields = ('id',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.section_type == 'single_image':
            data['content'] = SingleImageContentSerializer(instance.single_image_content).data
            # Remove the double image content from the response
            data.pop('double_image_content')
            # Remove the single image content from the response
            data.pop('single_image_content')
        elif instance.section_type == 'double_image':
            data['content'] = DoubleImageContentSerializer(instance.double_image_content).data
            # Remove the double image content from the response
            data.pop('double_image_content')
            # Remove the single image content from the response
            data.pop('single_image_content')
        return data
