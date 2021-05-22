import json
from holidays.models import *


def discountamount(request, package):
    price = []
    discount = []
    for i in package:
        offer = offers.objects.filter(package=i)
        if offer.exists():
            discountedoffer = offers.objects.get(package=i)
            discount.append(discountedoffer.discount_percentage)
            prices = (i.package_price) - \
                (((discountedoffer.discount_percentage)*(i.package_price))/100)
            price.append(prices)

        else:
            price.append(i.package_price)
            discount.append(0)
    return price, discount


def tourscalculate(request, destination):
    tours_list = []
    tours = 0
    for i in destination:
        name_tour = i.name
        tour = packages.objects.all()
        for t in tour:
            name_package = t.package_country
            if (name_package.lower() == name_tour.lower()) | (t.package_city.lower() == name_tour.lower()):
                tours += 1
        tours_list.append(tours)
        tours = 0

    return tours_list


def tourstype(request, package):
    international_list = []
    domestic_list = []

    for i in package:
        if "international" in i.package_type:
            international_list.append(i)
        elif "domestic" in i.package_type:
            domestic_list.append(i)
        else:
            pass

    return international_list, domestic_list


def discountamounttrending(request, trending):
    price = []
    discount = []
    for i in trending:
        offer = offers.objects.filter(package=i.package)
        if offer.exists():
            discountedoffer = offers.objects.get(package=i.package)
            discount.append(discountedoffer.discount_percentage)
            prices = (i.package.package_price) - \
                (((discountedoffer.discount_percentage)*(i.package.package_price))/100)
            price.append(prices)

        else:
            price.append(i.package.package_price)
            discount.append(0)
    return price, discount


def discountamountforapackage(request, package):
    offer = offers.objects.filter(package=package)
    if offer.exists():
        discountedoffer = offers.objects.get(package=package)
        discount = discountedoffer.discount_percentage
        price = (package.package_price) - \
            (((discountedoffer.discount_percentage)*(package.package_price))/100)
    else:
        price = package.package_price
        discount = 0
    return price, discount


def rating(request, package):
    rates = []
    review = []

    for i in package:
        ratings = reviews.objects.filter(packages=i)
        if ratings.exists():
            review.append(ratings.count())
            sum_star = sum([j.star for j in ratings])
            rat = (sum_star/ratings.count())
            rat = round(rat, 2)
            rates.append(rat)
            print("package_title=", i.package_title, "rates =", rat)
            print("reviews=", ratings.count())
        else:
            rates.append(0)
            review.append(0)
            print("reviews not present")
            print("package_title=", i.package_title)
            print("reviews=", ratings.count())

    return rates, review


def ratingfortrending(request, trending):
    rates = []
    review = []

    for i in trending:
        ratings = reviews.objects.filter(packages=i.package)
        if ratings.exists():
            review.append(ratings.count())
            sum_star = sum([j.star for j in ratings])
            rat = (sum_star/ratings.count())
            rat = round(rat, 2)
            rates.append(rat)
        else:
            rates.append(0)
            review.append(0)
            print("reviews not present")
            print("package_title=", i.package_title)
            print("reviews=", ratings.count())

    return rates, review


def ratingforapackage(request, package):
    i = package
    ratings = reviews.objects.filter(packages=i)
    if ratings.exists():
        review = ratings.count()
        sum_star = sum([j.star for j in ratings])
        rat = (sum_star/ratings.count())
        rat = round(rat, 2)
        rates = rat
        print("package_title=", i.package_title, "rates =", rat)
        print("reviews=", ratings.count())
    else:
        rates = 0
        review = 0
        print("reviews not present")
        print("package_title=", i.package_title)
        print("reviews=", ratings.count())

    return rates, review
