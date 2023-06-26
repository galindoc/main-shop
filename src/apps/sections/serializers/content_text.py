from rest_framework import serializers

from src.apps.sections.models import ContentText, Button


class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = (
            'id',
            'text',
            'link',
        )
        read_only_fields = (
            'id',
        )


class ContentTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentText
        fields = (
            'id',
            'text',
            'button',
        )
        read_only_fields = (
            'id',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.button:
            data['button'] = ButtonSerializer(instance.button).data
        return data
