"""
URL configuration for Inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from instruments import views as instrument_view
from students import views as student_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', instrument_view.home_view, name='home'),  # Set the root URL to the homepage in the instruments app
    path('', include('students.urls', namespace='students')),  # Add 'namespace' here
    path('', include('instruments.urls', namespace='instruments')),
    path('', include('checkout.urls', namespace='checkout')),
]
