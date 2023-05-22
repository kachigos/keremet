from django.urls import path
from .views import *

urlpatterns = [
    path('products/',ProductListView.as_view()),
    path('products/<int:pk>',ProductDetailView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('sub-categories/', SubCategoryListView.as_view()),
    path('categories/<int:category_id>/products/', CategoryProductListView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailView.as_view()),

]