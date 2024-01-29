from django.urls import path, include

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('order/', include('order.urls')),
]