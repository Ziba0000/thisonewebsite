from django.shortcuts import get_object_or_404, render, reverse, redirect
from .models import Order, OrderItem, Payment
from item.models import CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

@login_required
def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if cart_items:
        order = Order.objects.create(user=request.user)
        total_price = 0
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(order=order, item=cart_item.item, quantity=cart_item.quantity)
            total_price += cart_item.item.price * cart_item.quantity
            cart_item.delete()
        print(f"Order created: {order}")
        print(f"Total price: {total_price}")
        payment = Payment.objects.create(order=order, amount=total_price)
        print(f"Payment created: {payment}")
        return redirect(reverse('order:payment_page') + f'?order_id={order.id}')
    else:
        return redirect('item:view_cart')

@login_required
def view_orders(request):
    if request.method == 'POST' and 'delete_order' in request.POST:
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        if order.user == request.user:
            order.delete()
            return redirect('order:view_orders')

    orders = Order.objects.filter(user=request.user)
    order_items = [{'order': order, 'items': OrderItem.objects.filter(order=order)} for order in orders]
    return render(request, 'order/orders.html', {'order_items': order_items})

@login_required
def payment_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect('item:view_cart')

    total_price = sum(item.item.price * item.quantity for item in cart_items)
    return render(request, 'order/payment.html', {'total_price': total_price})

@login_required
def process_payment(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.item.price * item.quantity for item in cart_items)

        if cart_items:
            order = Order.objects.create(user=request.user)
            for cart_item in cart_items:
                OrderItem.objects.create(order=order, item=cart_item.item, quantity=cart_item.quantity)
            Payment.objects.create(order=order, amount=total_price)
            cart_items.delete()
            return redirect('order:view_orders')

    return HttpResponse(status=405)
