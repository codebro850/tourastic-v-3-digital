from holidays.models import *
from .utils import discountamount, tourscalculate, discountamountforapackage


def promocodeapply(request, promo, package):
    prcode = promocode.objects.filter(promo_code=promo)
    error_msg = ""
    price, discount = discountamountforapackage(request, package)
    if prcode.exists():
        prco = promocode.objects.get(promo_code=promo)
        price, discount = discountamountforapackage(
            request, package)
        package_pric = package.package_price
        if price == package_pric:

            used_not = promo_used.objects.filter(
                user_used=request.user, promocode=prco)
            if not used_not.exists():
                prc = promocode.objects.get(promo_code=promo)
                promo_discount = (package_pric) - \
                    (prc.discount_percentage*package_pric)/100
                error_msg = "success"
            else:
                promo_discount = 0
                error_msg = "you are not eligible for this promocode"
        else:
            promo_discount = 0
            error_msg = "this package is not eligible for this"
    else:
        promo_discount = 0
        error_msg = "Invalid promocode"
    return error_msg, promo_discount
