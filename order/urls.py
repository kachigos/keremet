from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('cart/<int:pk>/', CartItemDetailView.as_view()),
    path('questions', QuestionView.as_view())
]