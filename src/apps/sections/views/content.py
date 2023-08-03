from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from src.apps.sections.models import SingleImageContent, DoubleImageContent
from src.apps.sections.serializers import SingleImageContentSerializer, DoubleImageContentSerializer


class DoubleImageContentViewSet(ModelViewSet):
    queryset = DoubleImageContent.objects.all()
    serializer_class = DoubleImageContentSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        return Response(self.get_serializer(updated_instance).data)
    

class SingleImageContentViewSet(ModelViewSet):
    queryset = SingleImageContent.objects.all()
    serializer_class = SingleImageContentSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        return Response(self.get_serializer(updated_instance).data)
