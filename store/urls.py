from django.urls import path
from .views.store import Store
from .views.cart import Cart
from .views.pay import Pay

urlpatterns = [
    path('store/',Store.as_view(), name="store"),
    path('cart/',Cart.as_view(), name="cart"),
    path('pay/',Pay.as_view(), name="pay"),

    path('update_item/', Cart.updateItem, name="update_item"),
]