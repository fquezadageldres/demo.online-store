from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

import json

from ..models import *
from ..utils import *
from ..filters import *

# Create your views here.
class Pay(View):
    template_name = 'pay.html'

    def get(self, request, *args, **kwargs):
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']

        products = Product.objects.all()

        categoryFilter = orderFilters(request.GET, queryset=products)
        products = categoryFilter.qs

        context ={'items':items, 'products':products, 'order':order, 'cartItems': cartItems, 'categoryFilter':categoryFilter}
        return render(request, self.template_name, context)

    def updateItem(request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

        customer = request.user.customer
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        OrderItem, create = orderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            OrderItem.quantity = (OrderItem.quantity + 1)
        elif action == 'remove':
            OrderItem.quantity = (OrderItem.quantity - 1)

        OrderItem.save()

        if OrderItem.quantity <= 0:
            OrderItem.delete()

        return JsonResponse('Producto añadido', safe=False)
