import uuid, secrets

from slugify import slugify
from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    quantity = models.IntegerField(blank=False)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=30, unique=True)

    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        related_name='products',
    )
    subcategory = models.ForeignKey(
        'categories.SubCategory',
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args,**kwargs):
        slug = slugify(f'{secrets.token_hex(8)}')
        similars_count = Product.objects.filter(slug=slug).count()
        while True:
            if not Product.objects.filter(slug=f'{slug}{similars_count}').exists():
                break
            similars_count += 1
        self.slug = f'{slug}{similars_count}'
        super(Product, self).save(*args, **kwargs)
