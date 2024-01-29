from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('view/', views.view_orders, name='view_orders'),
    path('payment/', views.payment_page, name='payment_page'),
    path('process/', views.process_payment, name='process_payment'),
]
