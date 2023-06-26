from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from src.apps.sections.models import ContentImage
from src.apps.sections.serializers import ContentImageSerializer


class ContentImageViewSet(ModelViewSet):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        return Response(self.get_serializer(updated_instance).data)
