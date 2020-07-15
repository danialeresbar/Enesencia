from django.contrib.admin import register, ModelAdmin
from .models import Product


@register(Product)
class ProductAdmin(ModelAdmin):
    model = Product
    readonly_fields = ['slug', 'created', 'updated']
    list_display = ('__str__', 'slug')
