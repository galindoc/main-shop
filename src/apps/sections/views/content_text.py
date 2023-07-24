from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from src.apps.sections.serializers import ContentTextSerializer, ButtonSerializer
from src.apps.sections.models import ContentText, Button


class ButtonViewSet(ModelViewSet):
    queryset = Button.objects.all()
    serializer_class = ButtonSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        return Response(self.get_serializer(updated_instance).data)


class ContentTextViewSet(ModelViewSet):
    queryset = ContentText.objects.all()
    serializer_class = ContentTextSerializer
