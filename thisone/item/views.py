from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, CartItem

@login_required
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/detail.html', {'item': item})

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.item.price * item.quantity for item in cart_items)
    return render(request, 'item/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(item=item, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('item:view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('item:view_cart')
