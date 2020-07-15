from django import template
import locale


register = template.Library()


@register.filter()
def price_format(value):
    locale.setlocale(locale.LC_ALL, '')
    return "COP ${}".format(
        locale.format('%.2f', value, grouping=True, monetary=True)
    )
