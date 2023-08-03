import os
import requests
from django.core.files.base import ContentFile
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.core.settings')

application = get_wsgi_application()

from src.apps.products.models import Product, ProductImage
from src.apps.categories.models import Category, SubCategory

# Constants
price = 123
description = "Quisque neque mauris, fermentum sit amet magna ac, pulvinar finibus nisi. Duis quis accumsan sapien, vitae iaculis risus. Phasellus nec cursus nisi, eu rhoncus mi."
quantity = 20

# URLs for the images
image_urls = [
    "https://tenderi-media.s3.amazonaws.com/product_images/s_i_1.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZ5QGI42YRNKU3XF4%2F20230802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230802T235019Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=b5842e0a500747ae65ba2b6a9769b90ebdf33e16b8eb4277afcdc7e0b4d9dd1c",
    "https://tenderi-media.s3.amazonaws.com/product_images/s_i_2.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZ5QGI42YRNKU3XF4%2F20230802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230802T235035Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=aa4d53418516f53d539ab9b0cec41916895b896493c5026f69fbd78ac2b16bdc",
    "https://tenderi-media.s3.amazonaws.com/product_images/s_i_3.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZ5QGI42YRNKU3XF4%2F20230802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230802T234932Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=c28a8fc57629f2d06ab43260d7c61176f3fd508ec4dfcc9f6daa490a0e6f70a6",
    "https://tenderi-media.s3.amazonaws.com/product_images/s_i_4.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZ5QGI42YRNKU3XF4%2F20230802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230802T235004Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=ee4f33007ebfceea2a0c881196f12904022849a5eb51d69f618d9cf8c0ebe880"
]

categories = {
    "Ropa": {
        "subcategories": ["vestidos", "pantalones", "blusas"],
    },
    "Maquillaje": {
        "subcategories": ["labiales", "sombras", "bases"],
    },
    "Accesorios": {
        "subcategories": ["collares", "aretes", "anillos"],
    },
    "Cuidado Personal": {
        "subcategories": ["perfumes", "lociones", "mascarillas"],
    },
}

for category_name, subcategory_dict in categories.items():
    category, _ = Category.objects.get_or_create(name=category_name)
    print("Creating products for category", category_name)
    for subcategory_name in subcategory_dict['subcategories']:
        subcategory, _ = SubCategory.objects.get_or_create(name=subcategory_name, category=category)
        
        for i in range(1, 16):  # 15 products per subcategory
            # Create product
            product_name = f"{subcategory_name} sample {i}"
            product = Product(
                name=product_name,
                description=description,
                price=price,
                quantity=quantity,
                category=category,
                subcategory=subcategory
            )
            product.save()

            # Download and create product images
            for j, url in enumerate(image_urls, 1):
                response = requests.get(url)
                if response.status_code == 200:
                    product_image = ProductImage(product=product)
                    product_image.image.save(f"product_image_{subcategory_name}_{i}_{j}.webp", ContentFile(response.content))
                    product_image.save()
                else:
                    print(f"Failed to download the image {j} for product {i} in subcategory {subcategory_name}.")
