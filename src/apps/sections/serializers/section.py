from rest_framework import serializers

from src.apps.sections.models import Section
from src.apps.sections.serializers import ContentSerializer


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        read_only_fields = ('id',)

    def validate(self, attrs):
        # Validate if contents width sum is exactly 100
        contents = attrs.get('contents')
        if contents:
            contents_width_sum = sum([content.width for content in contents])
            if contents_width_sum != 100:
                raise serializers.ValidationError('Contents width sum must be exactly 100. Current sum is {}'.format(contents_width_sum))
            
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['contents'] = ContentSerializer(instance.contents.all(), many=True).data
        return data
