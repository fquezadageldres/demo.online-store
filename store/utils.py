import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {'cart_total_price':0,'cart_total_quantity':0}
    cartItems = order['cart_total_quantity']
    customer = ''
    
    for i in cart:
        cartItems += cart[i]["cantidad"]

        product = Product.objects.get(id=i)
        total = (product.price * cart[i]['cantidad'])

        order['cart_total_price'] += total
        order['cart_total_quantity'] += cart[i]['cantidad']

        item = {
            'product':{
                'id': product.id,
                'name':product.name,
                'price':product.price,
                'img':product.img,
            },
            'quantity':cart[i]['cantidad'],
            'get_total_item':total,
        }
        items.append(item)
    return {'cartItems':cartItems, 'order':order, 'items':items, 'customer': customer}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.cart_total_quantity
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
        customer = cookieData['customer']
        

    return {'cartItems':cartItems, 'order':order, 'items':items, 'customer': customer}