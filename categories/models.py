from django.db import models
from django.utils.text import slugify
from products.models import Product


class Category(models.Model):
    name = models.CharField(
        verbose_name="Nombre de la categoría",
        max_length=50
    )

    description = models.TextField(verbose_name="Descripción de la categoría")

    products = models.ManyToManyField(
        Product,
        verbose_name="Productos",
        blank=True
    )

    slug = models.SlugField(
        verbose_name="Slug",
        null=False,
        blank=False,
        unique=True
    )

    created = models.DateTimeField(
        verbose_name="Fecha de creación",
        auto_now_add=True
    )
    
    updated = models.DateTimeField(
        verbose_name="Fecha de actualización",
        auto_now=True
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
