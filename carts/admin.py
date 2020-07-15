from django.contrib.admin import register, ModelAdmin
from .models import Cart


@register(Cart)
class CartAdmin(ModelAdmin):
    model = Cart
    readonly_fields = ['slug', 'created', 'updated']
    list_display = ('__str__', 'slug')
