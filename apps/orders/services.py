from django.db import transaction
from .models import Order, OrderItem
from apps.cart.models import Cart


@transaction.atomic
def create_order_from_cart(user):
    cart = Cart.objects.get(user=user)

    order = Order.objects.create(user=user)

    total = 0

    for item in cart.items.all():
        price = item.book.price

        OrderItem.objects.create(
            order=order,
            book=item.book,
            quantity=item.quantity,
            price_at_purchase=price
        )

        total += price * item.quantity

    order.total_price = total
    order.save()

    cart.items.all().delete()

    return order