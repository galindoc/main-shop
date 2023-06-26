from rest_framework import viewsets, parsers, status
from rest_framework.response import Response

from src.apps.products.models import Product, ProductImage
from src.apps.products.serializers import ProductSerializer, ProductImageSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Get the list of image files from the request
        images = request.FILES.getlist('images')

        # Delete old images that are not in the new images list
        old_images = instance.images.all()
        for old_image in old_images:
            if old_image.image not in images:
                old_image.delete()

        # Process the new image files and save them as ProductImage instances
        product_images = []
        for image in images:
            product_image = ProductImage(product=instance, image=image)
            product_image.save()
            product_images.append(product_image)

        # Update the product instance and save it
        serializer = ProductSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save(images=product_images)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    