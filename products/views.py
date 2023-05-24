from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .filters import ProductFilter
from .serializers import*

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name', 'sub_category__name', 'name']

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class CategoryProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['category__name', 'sub_category__name', 'name']

    def get_queryset(self):
        category = self.kwargs['category_id']
        return Product.objects.filter(category=category)

class CategoryDetailView(generics.ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        category = self.kwargs['category_id']
        return SubCategory.objects.filter(category=category)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
