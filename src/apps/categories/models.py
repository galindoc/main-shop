import uuid

from django.db import models
from slugify import slugify

# Create a new model called Category that can be related to many products.

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30, unique=True)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def save(self, *args,**kwargs):
        slug = slugify(f'{self.name}')
        similars_count = Category.objects.filter(slug=slug).count()
        while True:
            if not Category.objects.filter(slug=f'{slug}{similars_count}').exists():
                break
            similars_count += 1
        self.slug = f'{slug}{similars_count}'
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30, unique=True)
    category = models.ForeignKey(
        'categories.Category', 
        on_delete=models.CASCADE,
        related_name='subcategories'
    )
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'subcategories'

    def save(self, *args,**kwargs):
        slug = slugify(f'{self.name}')
        similars_count = SubCategory.objects.filter(slug=slug).count()
        while True:
            if not SubCategory.objects.filter(slug=f'{slug}{similars_count}').exists():
                break
            similars_count += 1
        self.slug = f'{slug}{similars_count}'
        super(SubCategory, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
