from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.utils.text import slugify
from users.models import User
from products.models import Product
import decimal
import uuid


FEE = 0.05  # Comisión


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    products = models.ManyToManyField(
        Product
    )

    subtotal = models.DecimalField(
        verbose_name="Subtotal",
        default=0.0,
        max_digits=10,
        decimal_places=2
    )

    total = models.DecimalField(
        verbose_name="Subtotal",
        default=0.0,
        max_digits=10,
        decimal_places=2
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
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

    def __str__(self):
        return 'test_cart'

    def update_subtotal(self):
        self.subtotal = sum(
            [product.price for product in self.products.all()]
        )
        self.save(update_fields=["subtotal"])

    def update_total(self):
        global FEE
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(FEE))
        self.save(update_fields=["total"])

    def update_amount(self):
        self.update_subtotal()
        self.update_total()

    def save(self, *args, **kwargs):
        self.slug = slugify("carrito {}".format(str(uuid.uuid4())))
        super(Cart, self).save(*args, **kwargs)


@receiver(m2m_changed, sender=Cart.products.through)
def update_totals(sender, instance, action, *args, **kwargs):
    print("Señal emitida")
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_amount()
