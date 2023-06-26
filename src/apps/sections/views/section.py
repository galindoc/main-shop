from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from src.apps.sections.serializers import SectionSerializer
from src.apps.sections.models import Section, Content


class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        return Response(self.get_serializer(updated_instance).data)
    
    def add_content(self, request, *args, **kwargs):
        instance = self.get_object()
        content_id = request.data.get('content_id')
        try:
            content = instance.contents.get(pk=content_id)
            instance.contents.add(content)
            return Response(self.get_serializer(instance).data)
        except Content.DoesNotExist:
            return Response({"detail": "Content not found in the section's contents."}, status=status.HTTP_404_NOT_FOUND)
    
    def remove_content(self, request, *args, **kwargs):
        instance = self.get_object()
        content_id = request.data.get('content_id')
        try:
            content = instance.contents.get(pk=content_id)
            instance.contents.remove(content)
            return Response(self.get_serializer(instance).data)
        except Content.DoesNotExist:
            return Response({"detail": "Content not found in the section's contents."}, status=status.HTTP_404_NOT_FOUND)
