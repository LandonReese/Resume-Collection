from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('checkout/', views.checkout_index, name='checkout_index'),
    path('checkout/add/', views.add_checkout, name='add_checkout'),
    path('checkout/<int:checkout_id>/', views.view_checkout, name='view_checkout'),
    path('checkout/<int:checkout_id>/edit/', views.edit_checkout, name='edit_checkout'),
]
