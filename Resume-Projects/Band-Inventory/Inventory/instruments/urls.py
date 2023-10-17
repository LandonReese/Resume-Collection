from django.urls import path
from . import views

app_name = 'instruments'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('instruments/', views.instrument_index, name='instrument_index'),
    path('instruments/add/', views.add_instrument, name='add_instrument'),
    path('instruments/<int:instrument_id>/', views.view_instrument, name='view_instrument'),
    path('instruments/<int:instrument_id>/edit/', views.edit_instrument, name='edit_instrument'),
    path('instruments/delete/', views.delete_index, name='delete_index'),
] 