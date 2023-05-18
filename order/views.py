from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from .serializers import *
from .utils import send_telegram_message

class CartView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        session_id = self.request.session.session_key
        return CartItem.objects.filter(session_id=session_id)

    def post(self, request, *args, **kwargs):
        session_id = self.request.session.session_key
        if not session_id:
            self.request.session.save()
            session_id = self.request.session.session_key

        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart = self.get_queryset()
        cart_item = cart.filter(product=product).first()
        if cart_item:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(product=product, quantity=quantity, session_id=session_id)

        serializer = self.get_serializer(cart_item)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def put(self, request, *args, **kwargs):
        session_id = self.request.session.session_key
        if not session_id:
            self.request.session.save()
            session_id = self.request.session.session_key

        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity'))
        cart = self.get_queryset()
        cart_item = cart.filter(product_id=product_id).first()
        if cart_item:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(product_id=product_id, quantity=quantity, session_id=session_id)

        serializer = self.get_serializer(cart_item)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def delete(self, request, *args, **kwargs):
        session_id = self.request.session.session_key
        if not session_id:
            self.request.session.save()
            session_id = self.request.session.session_key

        product_id = request.data.get('product_id')
        cart = self.get_queryset()
        cart_item = cart.filter(product_id=product_id).first()
        if cart_item:
            cart_item.delete()

        return Response(status=204)


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'pk'

    def get_object(self):
        session_id = self.request.session.session_key
        cart_item = get_object_or_404(self.get_queryset(), pk=self.kwargs.get(self.lookup_field), session_id=session_id)
        return cart_item

class QuestionView(generics.CreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = request.data
        message_text = "Ticket booking:\n"
        for key, value in data.items():
            if key in ["username", "phone"]:
                message_text += f"{key}: {value}\n"
        send_telegram_message(message_text)
        return response