from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse, response
from holidays.models import *
from .utils import discountamount, tourscalculate, tourstype, discountamounttrending, discountamountforapackage
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login, logout
import json
from .cart import *
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .affiliate import *
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from tourastic.settings import EMAIL_HOST_USER
from .payment import *
from datetime import datetime, timedelta
from .cart import cartData
from .utils import *
from .promocode import *
from .currency import *
import re
# Create your views here.
import razorpay
client = razorpay.Client(
    auth=("rzp_test_ohASjZactVTRw1", "KZYl8XfZRRCREYkAXo8gxs6e"))


def index(request):
    package = packages.objects.all()
    test(request)
    prices = []
    price, discount = discountamount(request, package)
    ratings, reviews = rating(request, package)
    banner_b = banner.objects.all()
    service = services.objects.all()
    destiny = destinations.objects.all()
    curr = request.session.get("curr")
    # if curr == "":
    curr = "INR"
    print(curr)
    if (curr == "INR") | (curr == "inr"):
        zipped_package = zip(package, price, discount, ratings, reviews)
    else:
        # rate = currency_convert(request, "INR", curr)
        # [prices.append(round((float(rate)*(float(i))), 2)) for i in price]
        prices = price
        zipped_package = zip(package, prices, discount, ratings, reviews)
    # zipped_package = zip(package, price, discount, ratings, reviews)
    tours = tourscalculate(request, destiny)
    destination_zip = zip(destiny, tours)
    # print(request.session.get_expiry_date())
    data = cartData(request)
    cartitems = data['cartItems']
    print("cartitems=", cartitems)
    # country, currency_code = countryget(request)
    # prices = []
    # if currency_code == "INR":
    #     rate = currency_convert(request, "INR", "USD")
    #     [prices.append(round((float(rate)*(float(i))), 2)) for i in price]
    #     zipped_package = zip(package, prices, discount, ratings, reviews)
    # else:

    testimonials = testimonial.objects.all()
    members = teammembers.objects.all()
    # price=packages.offer_package
    return render(request, "index.html", {'package': zipped_package, 'banner': banner_b, 'destinations': destination_zip, 'services': service, 'destination': destiny, 'trendingtours': zipped_package, 'trending': package, "cartitems": cartitems, 'testimonial': testimonials, 'members': members, "currency": curr})


def logins(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                test(request)
                cookiecarttouser(request)
                return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message": "inactive"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "invalid"}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "denied"}), content_type="application/json")


def logouts(request):
    if User is not None:
        logout(request)
        return redirect("/")
    else:

        return redirect("/")


def signup(request):
    if request.method == "POST":
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        # data = {'first_name': fname, 'last_name': lname, 'email': email,
        #         'password2': password2, 'password1': password1}
        # form = SignUpForm(data=data)

        #     if form.is_valid():
        #         user = form.save(commit=False)
        #         user.is_active = True
        #         user.save()
        #         return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
        #     else:
        #         return HttpResponse(json.dumps({"message": form.errors}), content_type="application/json")
        # else:
        #     form = SignUpForm()
        # return HttpResponse(json.dumps({"message": "Denied"}), content_type="application/json")

        if User.objects.filter(username__iexact=username).exists():
            return HttpResponse(json.dumps({"message": "Username exists please try another username"}), content_type="application/json")
        elif User.objects.filter(email__iexact=username).exists():
            return HttpResponse(json.dumps({"message": "email exists"}), content_type="application/json")
        else:
            user = User.objects.create_user(
                username=username, password=password1, first_name=fname, last_name=lname, email=email)
            user.save()
            iser = authenticate(username=username, password=password1)
            if iser is not None:
                login(request, iser)
                test(request)
                cookiecarttouser(request)
                return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message": "Denied"}), content_type="application/json")

    return HttpResponse(json.dumps({"message": "Denied"}), content_type="application/json")


def usernamecheck(request):
    if request.method == "POST":
        username = request.POST.get("username")
        # print(request.user.username)
        if (User.objects.filter(username__iexact=username).exists()) & (username != request.user.username):
            return HttpResponse(json.dumps({"message": "taken"}), content_type="application/json")
        else:
            usser = User.objects.get(username=request.user.username)
            if username != request.user.username:
                usser.username = username
                usser.save()

            return HttpResponse(json.dumps({"message": "success"}), content_type="application/json")


def emailcheck(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # print(request.user.username)
        if (User.objects.filter(email__iexact=email).exists()) & (email != request.user.email):
            return HttpResponse(json.dumps({"message": "taken"}), content_type="application/json")
        else:
            usser = User.objects.get(username=request.user.username)
            if email != request.user.email:
                usser.email = email
                usser.save()
            return HttpResponse(json.dumps({"message": "success"}), content_type="application/json")


def addresssave(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            mobile = request.POST.get("mobile")
            country = request.POST.get("country")
            zipcode = request.POST.get("zipcode")
            address = request.POST.get("address")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            city = request.POST.get("city")
            state = request.POST.get("state")
            username = request.POST.get("username")
            email = request.POST.get("email")
            userinfos, created = userinfo.objects.get_or_create(
                users=request.user)
            userinfos.mobile_no = mobile
            userinfos.pincode = zipcode
            userinfos.country = country
            userinfos.address = address
            userinfos.city = city
            userinfos.state = state
            userinfos.save()
            usser = User.objects.get(username=request.user.username)
            usser.first_name = first_name
            usser.last_name = last_name
            usser.save()

            return HttpResponse(json.dumps({"message": "success"}), content_type="application/json")

        else:
            return HttpResponse(json.dumps({"message": "Denied"}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "Denied"}), content_type="application/json")


def profile(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        usser = User.objects.get(username=request.user.username)
        data = cartData(request)
        cartitems = data['cartItems']
        userinfos, created = userinfo.objects.get_or_create(users=request.user)
        return render(request, "user-profile.html", {"user": usser, "userinfo": userinfos, "cartitems": cartitems})


def packageinfo(request, package_name):
    package_name = re.sub(r'\W', "", package_name)
    packag = packages.objects.all()
    for i in packag:
        titles = (i.package_title).lower()
        titles = re.sub(r'\s', "", titles)
        if package_name.lower() == titles:
            price, discount = discountamountforapackage(request, i)
            promo_code = ""
            if request.user.is_authenticated:
                propmo = promo_process.objects.filter(
                    package=i, users=request.user, status="processing")

                if propmo.exists():
                    promos = promo_process.objects.get(
                        package=i, users=request.user, status="processing")
                    promo_code = promos.promo_cod.promo_code
                    price = promos.price_package
                    discount = promos.promo_cod.discount_percentage
            # country, currency_code = countryget(request)
            # if currency_code == "INR":
            #     rate = currency_convert(request, "INR", "USD")
            #     prices = (round((float(rate)*(float(price))), 2))
            #     zipped_package = {'tour':   package,
            #                       'price': prices, 'discount': discount}
            # else:
            curr = request.session.get("curr")
            # if curr == "":
            curr = "INR"
            if (curr == "INR") | (curr == "inr"):
                zipped_package = {'tour':   i,
                                  'price': price, 'discount': discount}
            else:
                # rate = currency_convert(request, "INR", curr)
                # [prices.append(round((float(rate)*(float(i))), 2)) for i in price]
                prices = price
                zipped_package = {'tour':   i,
                                  'price': prices, 'discount': discount}
            rating, reviews = ratingforapackage(request, i)
            # zipped_package = {'tour':   package,
            #                   'price': price, 'discount': discount}

            pak = json.dumps({"title": package_name})
            data = cartData(request)
            cartitems = data['cartItems']
            test(request)
            return render(request, "tours-display.html", {'package_info': i, "package": zipped_package, "pkd": pak, "cartitems": cartitems, "promocode": promo_code, "ratings": rating, "reviews": reviews, "currency": curr})
        else:
            pass


def contactpage(request):
    data = cartData(request)
    cartitems = data['cartItems']
    test(request)
    return render(request, "contact.html", {"cartitems": cartitems})


def blog(request):
    data = cartData(request)
    cartitems = data['cartItems']
    blo = blogs.objects.all()
    blogin = []
    commen = []
    for i in blo:
        bloin, created = bloginfo.objects.get_or_create(blog=i)
        blogin.append(bloin)
        comment = comments.objects.filter(blog=i)
        if comment.exists():
            commen.append(comment.count())
        else:
            pass

    test(request)
    bloi = zip(blo, blogin, commen)
    return render(request, "blog.html", {"cartitems": cartitems, "blogs": blo, "bloginfo": bloi})


def blogshow(request, blogname):
    blogname = re.sub(r'\W', "", blogname)
    bloi = blogs.objects.all()
    blos = []
    for i in bloi:
        titles = (i.title).lower()
        titles = re.sub(r'\s', "", titles)
        if blogname.lower() == titles:
            blos.append(i)
        return render(request, "blogs-demo.html", {"blogs": blos})


def history(request):
    history = []
    history_package = []
    if not request.user.is_anonymous:
        orders = order.objects.filter(customer=request.user, complete=True)
        if orders.exists():
            for i in orders:

                history.append(i)
                package = i.package
                oders = orderforpackage.objects.get(
                    order=i, username=request.user.username, package=package)
                history_package.append(oders)
        data = cartData(request)
        cartitems = data['cartItems']
        return render(request, "order-history.html", {"order_his": history, 'package_hist': history_package, "cartitems": cartitems})
    return redirect("/")


def saved(request):
    data = cartData(request)
    cartitems = data['cartItems']
    return render(request, "saved.html", {"cartitems": cartitems})


def destination(request, destination_name):
    destination = destinations.objects.get(name=destination_name)
    package = packages.objects.all()
    # if request.session.test_cookie_worked():
    #             print("The test cookie worked!!!")
    #             request.session.delete_test_cookie()
    # else:
    #     print('cookie not worked')
    pkg = []

    for i in package:
        if (i.package_country.lower() == destination_name.lower()) | (i.package_city.lower() == destination_name.lower()):
            pkg.append(i)
    price, discount = discountamount(request, pkg)
    ratings, reviews = rating(request, pkg)
    data = cartData(request)
    prices = []
    cartitems = data['cartItems']
    curr = request.session.get("curr")
    # if curr == "":
    curr = "INR"
    if (curr == "INR") | (curr == "inr"):
        zipped_package = zip(pkg, price, discount, ratings, reviews)
    else:
        # rate = currency_convert(request, "INR", curr)
        # [prices.append(round((float(rate)*(float(i))), 2)) for i in price]
        prices = price
        zipped_package = zip(pkg, prices, discount, ratings, reviews)
    # zipped_package = zip(pkg, price, discount)
    test(request)
    return render(request, "destinations.html", {'package': zipped_package, "destination": destination, "cartitems": cartitems, "currency": curr})


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    date = data['date_of_tour']
    passengers = data['passengers']
    child = data['child']
    infants = data['infants']
    customer = request.user
    product = packages.objects.get(package_title=productId)
    orders, created = order.objects.get_or_create(
        customer=customer, complete=False, package=product)

    orderItem, created = orderforpackage.objects.get_or_create(
        order=orders, package=product, username=request.user.username)
    price, discount = discountamountforapackage(request, product)
    propmo = promo_process.objects.filter(
        package=product, users=customer, status="processing")
    total = ((price*passengers)+((child*price)/2))
    if action == 'add':
        orderItem.passengers = passengers
        orderItem.child = child
        orderItem.infants = infants
        journeydate = date.replace("-", "/")
        journeydate = datetime.strptime(journeydate, "%Y/%m/%d").date()
        orderItem.date_tour = journeydate
        orderItem.daya_tour = product.package_duration
        orderItem.price_package = price
        orderItem.discount = discount
        orders.amout_paid = total
        orderItem.save()
        orders.save()
    elif action == 'remove':
        orderItem.delete()
        orders.delete()
    return JsonResponse('Item was added to cart', safe=False)


def cart(request):
    data = cartData(request)
    cartitems = data['cartItems']
    item = data['items']
    order = data['order']
    grant_total = data['grant_total']
    promo_code = []
    if not request.user.is_anonymous:
        for i in item:
            propmo = promo_process.objects.filter(
                package=i.package, users=request.user, status="processing")
            if propmo.exists():
                promos = promo_process.objects.get(
                    package=i.package, users=request.user, status="processing")
                promo_code.append(promos.promo_cod.promo_code)
    zipped = zip(item, promo_code)
    return render(request, "cart.html", {'orders': order, "cartitems": cartitems, "items": item, 'grant_total': grant_total, "zipped": zipped})


def tours(request):
    package = packages.objects.all()
    international, domestic = tourstype(request, package)
    price_domestic, discount_domestic = discountamount(request, domestic)
    rating_domestic, reviews_demoestic = rating(request, domestic)
    price_internatinal, discount_international = discountamount(
        request, international)
    ratings_international, reviews_international = rating(
        request, international)

    trending = trendingtours.objects.all()
    price_trending, discount_trending = discountamounttrending(
        request, trending)
    rating_trend, review_treend = ratingfortrending(request, trending)

    data = cartData(request)
    cartitems = data['cartItems']
    curr = request.session.get("curr")
    # if curr == "":
    curr = "INR"
    if (curr == "INR") | (curr == "inr"):
        domestic_package = zip(domestic, price_domestic,
                               discount_domestic, rating_domestic, reviews_demoestic)
        international_package = zip(
            international, price_internatinal, discount_international, ratings_international, reviews_international)
        zipped_package = zip(trending, price_trending,
                             discount_trending, rating_trend, review_treend)

    else:
        # rate = currency_convert(request, "INR", curr)
        # [prices.append(round((float(rate)*(float(i))), 2)) for i in price]
        price_domestics = price_domestic
        price_internatinals = price_internatinal
        price_trendings = price_trending
        domestic_package = zip(domestic, price_domestics,
                               discount_domestic, rating_domestic, reviews_demoestic)
        international_package = zip(
            international, price_internatinals, discount_international, ratings_international, reviews_international)
        zipped_package = zip(trending, price_trendings,
                             discount_trending, rating_trend, review_treend)
    test(request)
    return render(request, "tour-packages.html", {"international": international_package, "domestic": domestic_package, "trending": zipped_package, "cartitems": cartitems, "currency": curr})


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = request.POST.get('email')
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "emailreset.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'tourastic',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, EMAIL_HOST_USER,
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse(json.dumps({"message": "Invalid header found."}), content_type="application/json")

                    return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")

    password_reset_form = PasswordResetForm()
    return HttpResponse(json.dumps({"message": "error"}), content_type="application/json")


def messagesend(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        messag = request.POST.get('message')
        messagss = messagess.objects.create(
            name=name, email=email, subject=subject, messages=messag)
        messagss.save()
        try:
            send_mail("Thanks for contacting", "Thanks for contacting us we will revert back to you as soon as possible", EMAIL_HOST_USER,
                      [email], fail_silently=False)
        except BadHeaderError:
            return HttpResponse(json.dumps({"message": "Invalid header found."}), content_type="application/json")
        return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "error"}), content_type="application/json")


def create_order(request, package_title):
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'
    package = packages.objects.get(package_title=package_title)
    price, discount = discountamountforapackage(request, package)
    promo_dis = 0
    if not request.user.is_anonymous:
        propmo = promo_process.objects.filter(
            package=package, users=request.user, status="processing")
        if propmo.exists():
            promos = promo_process.objects.get(
                package=package, users=request.user, status="processing")
            if discount == 0:

                prices = (
                    price-((price*promos.promo_cod.discount_percentage)/100))
                promo_dis = (price-prices)
                price = prices

    orders = order.objects.get(
        customer=request.user, complete=False, package=package)
    orderItem = orderforpackage.objects.get(
        order=orders, package=package, username=request.user.username, order_status="processing")
    order_amount = orderItem.get_total
    print(order_amount)
    # CREAING ORDER
    response = client.order.create(dict(
        amount=order_amount, currency=order_currency, receipt=order_receipt,  payment_capture='0'))

    order_id = response['id']
    order_status = response['status']
    if order_status == 'created':
        orders.order_id = order_id
        orders.amout_paid = order_amount
        orders.save()
    # package_details = {'packager': package,
    #                    'price': price, 'total': order_amount, 'discount': discount}
    data = cartData(request)
    cartitems = data['cartItems']
    promo_code = ""

    if not request.user.is_anonymous:
        propmo = promo_process.objects.filter(
            package=orderItem.package, users=request.user, status="processing")
        if propmo.exists():
            promos = promo_process.objects.get(
                package=orderItem.package, users=request.user, status="processing")
            promo_code = promos.promo_cod.promo_code

    if order_status == 'created':
        return render(request, "confirm_order.html", {"package": package,
                                                      'price': price, 'items': orderItem, "promocode": promo_code, 'order_amount': order_amount, 'discount': discount, 'order_id': order_id, "promodis": promo_dis, "cartitems": cartitems})

    return HttpResponse('<h1>Error in  create order function</h1>')


def payment_status(request):

    response = request.POST

    params_dict = {
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    orders = order.objects.get(order_id=params_dict['razorpay_order_id'])
    orderItems = orderforpackage.objects.get(order=orders)
    packag = orders.package
    price_passengers = orderItems.price_package*orderItems.passengers
    price_child = (orderItems.child*orderItems.price_package)/2
    price_infants = orderItems.infants*0
    price, discount = discountamountforapackage(request, packag)
    you_saved = (packag.package_price)-(price)
    you_saved_total = ((orderItems.passengers*packag.package_price)-(orderItems.price_package*orderItems.passengers)) + \
        (((orderItems.child*packag.package_price)/2) -
         ((orderItems.child*orderItems.price_package)/2))
    child_amount = (orderItems.price_package)/2
    data = cartData(request)
    cartitems = data['cartItems']
    propmo = promo_process.objects.filter(
        package=packag, users=request.user, status="processing")
    if propmo.exists():
        promos = promo_process.objects.get(
            package=packag, users=request.user, status="processing")
        promocodess = promos.promo_cod
        promo_code = promos.promo_cod.promo_code
        promos.status = "completed"
        promoss = promo_used.objects.create(
            package=packag, promocode=promocodess, user_used=request.user)
        promoss.save()
    # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        orders.transaction_id = params_dict['razorpay_payment_id']
        orders.complete = True
        orderItems.order_status = "completed"
        orders.save()
        orderItems.save()
        affiliate_check(request, request.user,
                        params_dict['razorpay_payment_id'])

        return render(request, 'order_summary.html', {'status': 'Payment Successful', 'orderItems': orderItems, 'orders': orders, 'price_passengers': price_passengers, 'price_child': price_child, 'price_infants': price_infants, 'you_saved': you_saved, 'you_saved_total': you_saved_total, 'discount': discount, 'child_amount': child_amount, "cartitems": cartitems})
    except:

        return render(request, 'order_summary.html', {'status': "payment failed!!"})


def book(request, package_title):
    if request.method == "POST":
        if request.user.is_anonymous:
            return HttpResponse(json.dumps({"message": 'login required'}), content_type="application/json")
        else:
            dateofjourney = request.POST.get('dateoftravel')
            journeydate = dateofjourney.replace("-", "/")
            journeydate = datetime.strptime(journeydate, "%Y/%m/%d").date()
            adults = request.POST.get('adult')
            child = request.POST.get('child')
            infants = request.POST.get('infants')
            package = packages.objects.get(package_title=package_title)
            # daysoftour = package.package_duration
            price, discount = discountamountforapackage(request, package)
            if not request.user.is_anonymous:
                propmo = promo_process.objects.filter(
                    package=package, users=request.user, status="processing")
                if propmo.exists():
                    promos = promo_process.objects.get(
                        package=package, users=request.user, status="processing")
                    if discount == 0:
                        price = (
                            price-((price*promos.promo_cod.discount_percentage)/100))

            orders, created = order.objects.get_or_create(
                customer=request.user, complete=False, package=package)
            orderItem, created = orderforpackage.objects.get_or_create(
                order=orders, package=package, username=request.user.username)
            orderItem.passengers = adults

            orderItem.child = child
            orderItem.infants = infants
            orderItem.daya_tour = package.package_duration
            orderItem.date_tour = journeydate
            orderItem.price_package = price
            orderItem.enddate_tour = journeydate + \
                timedelta(package.package_duration)
            orderItem.order_status = "processing"

            orderItem.save()
            orders.save()
            # items = orders.orderforpackage_set.all()
            # total = orderItem.get_total
            # print(total)
            # create_order(request, total, package)
            passengerss = int(child)+int(infants)+int(adults)
            url = "/details/"+package_title+"/?"+"p="+str(passengerss)
            return HttpResponse(json.dumps({"message": {"sucess": "success", "url": url}}), content_type="application/json")
        # check, transaction_id = create_order(request, total)
        # if check:

        #     package_details = {'packager': package,
       #                        'price': price, 'total': total, 'discount': discount}
        #     return redirect('confirm_order/'+package.package_title+"/"+transaction_id+"/")

        # return HttpResponse(json.dumps({"message": "error"}), content_type="application/json")


def promo(request):
    if request.method == "POST":
        promo_code = request.POST.get("promocode")
        package_title = request.POST.get("title")
        package = packages.objects.get(package_title=package_title)
        msg, promo_discount = promocodeapply(request, promo_code, package)
        if msg == "success":
            promoc = promocode.objects.get(promo_code=promo_code)
            promop, created = promo_process.objects.get_or_create(
                package=package, users=request.user, promo_cod=promoc, status="processing", price_package=promo_discount)
            return HttpResponse(json.dumps({"message":  "success", "discount": str(promop.promo_cod.discount_percentage)}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": msg}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "error"}), content_type="application/json")


def searchdestiny(request):
    if request.method == "POST":
        destiny = request.POST.get("dname")
        dateoftour = request.POST.get("ddate")
        enddateoftour = request.POST.get("edate")
        price_range = request.POST.get("dprice")
        print(price_range)
        if price_range != "":
            b, c = (str(price_range)).split("-")
            d, e = b.split("Rs. ")
            f = e.replace(",", "")
            price_filter_lower = round((float(f)), 2)
            c = c.replace(",", "")
            price_filter_upper = round((float(c)), 2)
        package = packages.objects.all()
        # price, discount = discountamount(request, package)
        # ratings, reviews = rating(request, package)
        tours = []
        discounts = []
        prices = []
        country = ""
        tour = []
        rate = []
        revie = []
        pri = []
        dis = []
        ratingss = []
        reviewss = []
        for i in package:
            if (((i.package_title).lower()).__contains__((destiny).lower())) | (((i.package_country).lower()).__contains__((destiny).lower())) | (((i.package_city).lower()).__contains__((destiny).lower())) | (((i.package_desc).lower()).__contains__((destiny).lower())):
                j, k = discountamountforapackage(request, i)
                l, m = ratingforapackage(request, i)
                country = i.package_country
                if price_range != "":
                    if price_filter_lower <= j <= price_filter_upper:
                        print("price_filter:", i)
                        tours.append(i)
                        discounts.append(k)
                        ratingss.append(l)
                        prices.append(j)
                        reviewss.append(m)
                    else:
                        print("not price_filter:", i)
                        tours.append(i)
                        discounts.append(k)
                        ratingss.append(l)
                        prices.append(j)
                        reviewss.append(m)

                else:
                    print("not applied:", i)
                    tours.append(i)
                    discounts.append(k)
                    ratingss.append(l)
                    prices.append(j)
                    reviewss.append(m)
        # for j in package:
        #     if (j.package_country == country):

        #         j, k = discountamountforapackage(request, i)
        #         l, m = ratingforapackage(request, i)
        #         tour.append(j)
        #         rate.append(l)
        #         revie.append(m)
        #         pri.append(j)
        #         dis.append(k)

        data = cartData(request)
        cartitems = data['cartItems']
        curr = request.session.get("curr")
        # if curr == "":
        curr = "INR"
        if (curr == "INR") | (curr == "inr"):
            zipped_tours = zip(tours, prices, discounts, ratingss, reviewss)
        else:
            # rate = currency_convert(request, "INR", curr)
            # [prices.append(round((float(rate)*(float(i))), 2)) for i in price]
            pricess = prices
            zipped_tours = zip(tours, pricess, discounts, ratingss, reviewss)

        return render(request, "search.html", {"searchtours": zipped_tours, "cartitems": cartitems, "currency": curr})


def postingcurr(request):
    if request.method == "POST":
        curr = request.POST.get("curr")
        print(curr)
        sessioncreation(request, curr)
        return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message": "error"}), content_type="application/json")


def detailform(request, package_title):
    a = request.GET.get('p', '')
    if a == "":
        a = "1"

    passenger = ""
    for i in range(0, int(a)):
        passenger = passenger+str(i)

    return render(request, "detailform.html", {"passengers": passenger, "package_title": package_title})


def savingdat(request, pack):
    if request.method == "POST":
        print("inthe post request")
        mobile = request.POST.get("number")
        email = request.POST.get("email")
        alternate = request.POST.get("alternate")
        passenger_names = request.POST.getlist("pass_name[]")
        pass_age = request.POST.getlist("pass_age[]")
        pass_gender = request.POST.getlist("pass_gender[]")

        for i in range(0, len(passenger_names)):
            if passenger_names[i] == "":
                return HttpResponse(json.dumps({"message": "empty", "field": "passenger_name", "index": i}), content_type="application/json")
            if pass_age[i] == "":
                return HttpResponse(json.dumps({"message": "empty", "field": "age", "index": i}), content_type="application/json")
            if pass_gender[i] == "":
                return HttpResponse(json.dumps({"message": "empty", "field": "gender", "index": i}), content_type="application/json")
            else:
                pass
        packad = packages.objects.get(package_title=pack)
        orders, created = order.objects.get_or_create(
            customer=request.user, complete=False, package=packad)
        orderItem, created = orderforpackage.objects.get_or_create(
            order=orders, package=packad, username=request.user.username)
        # passengers_count = orderItem.child+orderItem.passengers+orderItem.infants
        type = "adult"
        for i in range(0, len(passenger_names)):
            if int(pass_age[i]) <= 2:
                type = "infant"
            if 2 < int(pass_age[i]) < 18:
                type = "child"
            if int(pass_age[i]) >= 18:
                type = "adult"
            passs = passengers.objects.create(
                pas=passenger_names[i], age=pass_age[i], gender=pass_gender[i], pass_type=type, package=packad)
            passs.save()
            pass_detail, created = passengers_details.objects.get_or_create(
                orders=orders)
            pass_detail.passenger.add(passs)
            pass_detail.save()
        url = "/confirm_order/"+pack
        return HttpResponse(json.dumps({"message": "success", "url": url}), content_type="application/json")

    # return HttpResponse(json.dumps({"message": "error"}), content_type="application/json")
