from rest_framework import generics, filters

from .models import *
from .serializers import*

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class CategoryProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name', 'sub_category__name', 'name']

    def get_queryset(self):
        category = self.kwargs['category_id']
        return Product.objects.filter(category=category)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
