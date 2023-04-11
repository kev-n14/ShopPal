"""shoppal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from shop.views import get_shop_list, add_item_shop_list, edit_item_shop_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_shop_list, name='get_shop_list'),
    path('add', add_item_shop_list, name='add'),
    path('edit/<item_id>', edit_item_shop_list, name='edit'),
]
