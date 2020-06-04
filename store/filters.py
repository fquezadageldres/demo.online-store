import django_filters
from .models import *

class orderFilters(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Menor precio'),
        ('descending', 'Mayor precio'),
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
        }
        exclude = ['desc', 'created_at', 'updated_at', 'img', 'digital']
    
    def filter_by_order(self, queryset, name, price):
        var = 'price' if price == 'ascending' else '-price'
        return queryset.order_by(var)
