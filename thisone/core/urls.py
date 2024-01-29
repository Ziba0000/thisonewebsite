from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', include('item.urls')),
    path('signup/', views.signup, name='signup'),
    path('order/', include('order.urls')),
    path('login/', views.login_user, name='login'),
    path('logout/', views.custom_logout, name='logout'),
]
