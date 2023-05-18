import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    categories = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    sub_categories = django_filters.CharFilter(field_name='sub_category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['categories', 'sub_categories']