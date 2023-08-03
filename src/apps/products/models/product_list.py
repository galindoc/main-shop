import uuid

from django.db import models
from slugify import slugify


class CustomProductList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args,**kwargs):
        slug = slugify(self.name)
        similars_count = CustomProductList.objects.filter(slug=slug).count()
        while True:
            if not CustomProductList.objects.filter(slug=f'{slug}{similars_count}').exists():
                break
            similars_count += 1
        self.slug = f'{slug}{similars_count}'
        super(CustomProductList, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product List'
        verbose_name_plural = 'Product Lists'

    def __str__(self):
        return f'{self.name} - {self.id}'
