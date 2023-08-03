from rest_framework import serializers

from src.apps.sections.models import Button, SingleImageContent, DoubleImageContent
from src.apps.sections.serializers import ButtonSerializer


class DoubleImageContentSerializer(serializers.ModelSerializer):
    button_left = ButtonSerializer(required=False)
    button_right = ButtonSerializer(required=False)

    class Meta:
        model = DoubleImageContent
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        button_left_data = validated_data.pop('button_left', None)
        button_right_data = validated_data.pop('button_right', None)
        content = DoubleImageContent.objects.create(**validated_data)

        if button_left_data:
            Button.objects.create(content=content, **button_left_data)

        if button_right_data:
            Button.objects.create(content=content, **button_right_data)

        return content
    
    def update(self, instance, validated_data):
        button_left_data = validated_data.pop('button_left', None)
        button_right_data = validated_data.pop('button_right', None)

        if button_left_data:
            button, created = Button.objects.get_or_create(content=instance)
            for attr, value in button_left_data.items():
                setattr(button, attr, value)
            button.save()

        if button_right_data:
            button, created = Button.objects.get_or_create(content=instance)
            for attr, value in button_right_data.items():
                setattr(button, attr, value)
            button.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance


class SingleImageContentSerializer(serializers.ModelSerializer):
    button = ButtonSerializer(required=False)

    class Meta:
        model = SingleImageContent
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        button_data = validated_data.pop('button', None)
        content = SingleImageContent.objects.create(**validated_data)

        if button_data:
            Button.objects.create(content=content, **button_data)

        return content
    
    def update(self, instance, validated_data):
        button_data = validated_data.pop('button', None)

        if button_data:
            button, created = Button.objects.get_or_create(content=instance)
            for attr, value in button_data.items():
                setattr(button, attr, value)
            button.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        
        return instance

