from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(
        verbose_name="Nombre del producto",
        max_length=50
    )

    description = models.TextField(verbose_name="Descripción del producto")
    product_image = models.ImageField(
        verbose_name="Imagen",
        upload_to='products/',
        null=False,
        blank=False
    )

    price = models.DecimalField(
        verbose_name="Precio",
        max_digits=8,
        decimal_places=2,
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
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
