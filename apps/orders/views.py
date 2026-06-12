from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from .services import create_order_from_cart
from apps.notifications.tasks import (
    send_order_confirmation_email
)

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        order = create_order_from_cart(request.user)
        serializer = self.get_serializer(order)

        send_order_confirmation_email.delay(
            user.email,
            order.id
        )
        

        return Response(serializer.data)