from django.contrib.admin import register, ModelAdmin
from .models import Category


@register(Category)
class CategoryAdmin(ModelAdmin):
    model = Category
    readonly_fields = ['slug', 'created', 'updated']
    list_display = ('__str__', 'slug')
