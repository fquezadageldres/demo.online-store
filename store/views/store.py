from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

import json

from ..models import *
from ..utils import *
from ..filters import *

# Create your views here..
class Store(View):
    template_name = 'store.html'

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