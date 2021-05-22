import json
from holidays.models import *
from .promocode import *
from .utils import *


def cookieCart(request):

    # Create empty cart for now for non-logged in user
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    item = []
    grant_total = 0
    orders = []
    cartItems = 0

    for i in cart:
        # We use try block to prevent items in cart that may have been removed from causing error
        try:
            if(cart[i]['passengers'] > 0):  # items with negative quantity = lot of freebies
                product = packages.objects.get(package_title=i)

                cartItems += 1
                price, discount = discountamountforapackage(request, product)
                total = cart[i]['passengers']*price
                grant_total += total
                print(total)
                print(product)
                # print(item.package.package_images)
                orders.append({"amout_paid": total, 'package': {'package_title': product.package_title, 'package_price': product.package_price,
                                                                ' package_images': product.package_images, 'package_desc': product.package_desc}, 'complete': False})
                items = {'productid': i, 'order': {"amout_paid": total, 'complete': False},
                         'package': {'package_title': product.package_title, 'package_price': product.package_price,
                                     'package_images': product.package_images, 'package_desc': product.package_desc},
                         'passengers': cart[i]['passengers'], 'child': 0, 'infants': 0, 'daya_tour': 4, 'date_tour': "1990/01/01", 'price_package': price, 'discount': discount}
                item.append(items)

        except Exception as e:
            print("exception not going")
            print(getattr(e, 'message', repr(e)))
            print(getattr(e, 'message', str(e)))
            pass

    return {'cartItems': cartItems, 'order': orders, 'items': item, "grant_total": grant_total}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user
        ordes = order.objects.filter(
            customer=customer, complete=False)
        orders = []
        items = []
        grant_total = 0
        cartItems = 0
        curr = request.session.get("curr")
        # if curr == "":
        curr = "INR"
        print(curr)
        if (curr == "INR") | (curr == "inr"):
            if ordes.exists():
                for i in ordes:
                    ites = orderforpackage.objects.filter(order=i)
                    grant_total += i.amout_paid
                    if ites.exists():
                        for j in ites:
                            items.append(j)
                            cartItems += 1
                    orders.append(i)

        else:
            # rate = currency_convert(request, "INR", curr)
            # [prices.append(round((float(rate)*(float(i))), 2)) for i in price]
            if ordes.exists():
                for i in ordes:
                    ites = orderforpackage.objects.filter(order=i)
                    grant_total += i.amout_paid
                    if ites.exists():
                        for j in ites:

                            items.append(j)
                            cartItems += 1
                    orders.append(i)
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        orders = cookieData['order']
        grant_total = cookieData['grant_total']
        items = cookieData['items']
    return {'cartItems': cartItems, 'order': orders, 'items': items, "grant_total": grant_total}


def cookiecarttouser(request):
    if request.user.is_authenticated:
        cookieData = cookieCart(request)
        # cartItems = cookieData['cartItems']
        orders = cookieData['order']
        # grant_total = cookieData['grant_total']
        items = cookieData['items']
        customer = request.user
        for i in items:
            productid = i['productid']
            product = packages.objects.get(package_title=productid)
            orders, created = order.objects.get_or_create(
                customer=customer, complete=False, package=product)
            orderItem, created = orderforpackage.objects.get_or_create(
                order=orders, package=product, username=request.user.username)
            orderItem.passengers = i['passengers']
            orderItem.child = 0
            orderItem.infants = 0
            date = "1990/01/01"
            price = i['price_package']
            discount = i['discount']
            total = i['order']['amout_paid']
            journeydate = date.replace("-", "/")
            journeydate = datetime.strptime(journeydate, "%Y/%m/%d").date()
            orderItem.date_tour = journeydate
            orderItem.daya_tour = product.package_duration
            orderItem.price_package = price
            orderItem.discount = discount
            orders.amout_paid = total
            orderItem.save()
            orders.save()
