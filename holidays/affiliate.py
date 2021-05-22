from .models import *
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone


def test(request):
    a = request.GET.get('id', '')
    if request.GET.get('id'):
        affly = affiliateaccounts.objects.filter(aid=a)
        if affly.exists():
            aff = affiliateaccounts.objects.get(aid=a)
            if request.user.is_authenticated:
                affiliate_register = affialiate_click.objects.filter(
                    affliateuser=aff, user=request.user)
                affiliate_info, created = affiliate_info_user.objects.get_or_create(
                    affliateuser=aff)
                user_exists = affialiate_click.objects.filter(
                    user=request.user)
                if 'aid' not in request.session:
                    if not user_exists.exists():
                        if not affiliate_register.exists():
                            rgs = affialiate_click.objects.create(
                                affliateuser=aff, user=request.user)
                            affiliate_info.visited = (affiliate_info.visited+1)
                            # user_exists=affialiate_click.objects.filter(user=request.user)
                            affiliate_info.logged_in_users = (
                                (affiliate_info.logged_in_users)+1)
                            affiliate_info.save()
                            rgs.save()

                else:
                    print("nothing to do for this")

            else:
                affiliate_info, created = affiliate_info_user.objects.get_or_create(
                    affliateuser=aff)
                if 'aid' not in request.session:
                    affiliate_info.visited = (affiliate_info.visited+1)
                    affiliate_info.save()

            if 'aid' not in request.session:
                print("yes it is in affiliate")
                request.session['aid'] = a
                print("something to store")
                # request.session['aff']['recorded']=datetime.now()
                request.session.set_expiry(2592000)

        else:
            print("not in affiliate")
    else:
        print("nothing in get request")

# This method is called whenever payment is done for purchase


def affiliate_check(request, username, transaction):
    aid = request.session.get("aid")
    affly = affiliateaccounts.objects.filter(aid=aid)
    if 'aid' in request.session:
        if affly.exists():
            aff = affiliateaccounts.objects.get(aid=aid)
            orders = order.objects.filter(
                transaction_id=transaction, customer=username)
            if orders.exists():
                sucess = affiliate_success.objects.filter(affiliateuser=aff,
                                                          successful_affiliate=username)
                if not sucess.exists():
                    odes = order.objects.get(
                        transaction_id=transaction, customer=username)
                    packge_order = orderforpackage.objects.get(
                        order=odes, package=odes.package)
                    amount_paid = packge_order.price_package
                    package = odes.package
                    amount_affiliate = ((amount_paid*10)/100)
                    print(amount_affiliate)
                    slr, created = affiliate_info_user.objects.get_or_create(
                        affliateuser=aff)
                    slr.ammount_received = (
                        slr.ammount_received+amount_affiliate)
                    slr.successfull_affiliate = (slr.successfull_affiliate+1)
                    suces = affiliate_success.objects.create(affiliateuser=aff, successful_affiliate=username, affiliate_product=package,
                                                             ammount_received=amount_paid, ammount_earned_affiliate=amount_affiliate, percentage_affiliate=10.00)
                    suces.save()
                    slr.save()
                else:
                    print("users benifit already given to the affiliate!")
    else:
        print("affiliate does not exists")
