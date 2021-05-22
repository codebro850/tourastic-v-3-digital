from django.contrib import admin
from holidays.models import packages, orderforpackage, hotels, transport, userinfo, blogs, comments
from holidays.models import *


class affiliate_display_suucess(admin.ModelAdmin):
    list_display = ('affiliateuser', 'successful_affiliate', 'affiliate_product',
                    'ammount_received', 'ammount_earned_affiliate', 'percentage_affiliate', 'date_affiliate_successfull')


class displaypacakgeservice(admin.ModelAdmin):
    list_display = ("service", "date_added")


class affiliate_display_click(admin.ModelAdmin):
    list_display = ('affliateuser', 'user', 'date_logged_in')


class affiliate_display_info(admin.ModelAdmin):
    list_display = ('affliateuser', 'visited', 'logged_in_users',
                    'successfull_affiliate', 'ammount_received', 'ammount_withdrawn', 'updated_on')


class affiliate_display_transaction(admin.ModelAdmin):
    list_display = ('affliateuser', 'ammount_withdrawn',
                    'ammount_left', 'transaction_id', 'date_of_transaction')


class affiliate_display_accounts(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'aid')


class displaypromo(admin.ModelAdmin):
    list_display = ('users', 'package', 'promo_cod', 'status', 'promo_added')


class promo_dis(admin.ModelAdmin):
    list_display = ('user_used', 'promocode', 'package', 'used_at')


class displaypromocode(admin.ModelAdmin):
    list_display = ('promo_code', 'discount_percentage', 'used_by_specific_user',
                    'used_for_all', 'user_for_promocode', 'time_created')


class trendingdisplay(admin.ModelAdmin):
    list_display = ('package', 'useradded', 'datetimecreated')


class dispalymessage(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'messages', 'messaged_at')


class userinfA(admin.ModelAdmin):
    list_display = ('users', 'address', 'mobile_no',
                    'pincode', 'country', 'datetime')


class packagesdisplay(admin.ModelAdmin):
    list_display = ('package_country', 'package_city', 'package_type',
                    'package_categories', 'package_duration', 'package_price')


class offerdisplay(admin.ModelAdmin):
    list_display = ('package', 'offer', 'discount_percentage',
                    'valid_to', 'created_at', 'created_by')


class orderdisplay(admin.ModelAdmin):
    list_display = ('customer', 'package', 'date_ordered',
                    'complete', 'transaction_id')


class orderforpackagedisplay(admin.ModelAdmin):
    list_display = ('username', 'order', 'package',
                    'date_ordered', 'order_status')


class reviewsdisplay(admin.ModelAdmin):
    list_display = ('star', 'packages', 'desc', 'user', 'datecreated')


# Register your models here.
admin.site.register(packages, packagesdisplay)
admin.site.register(orderforpackage, orderforpackagedisplay)
admin.site.register(hotels)
admin.site.register(transport)
admin.site.register(userinfo, userinfA)
admin.site.register(blogs)
admin.site.register(comments)
admin.site.register(offers, offerdisplay)
admin.site.register(order, orderdisplay)
admin.site.register(affiliateaccounts, affiliate_display_accounts)
admin.site.register(affiliateinfo)
admin.site.register(banner)
admin.site.register(reviews, reviewsdisplay)
admin.site.register(services)
admin.site.register(destinations)
admin.site.register(promocode, displaypromocode)
admin.site.register(promo_used, promo_dis)
admin.site.register(affialiate_click, affiliate_display_click)
admin.site.register(affiliate_info_user, affiliate_display_info)
admin.site.register(affiliate_success, affiliate_display_suucess)
admin.site.register(affiliate_transaction, affiliate_display_transaction)
admin.site.register(trendingtours, trendingdisplay)
admin.site.register(messagess, dispalymessage)
admin.site.register(promo_process, displaypromo)
admin.site.register(package_servicess, displaypacakgeservice)
admin.site.register(routines)
admin.site.register(testimonial)
admin.site.register(teammembers)
admin.site.register(passengers)
admin.site.register(passengers_details)
admin.site.register(bloginfo)
# admin customization

admin.site.site_header = "Tourastic Holidays"
admin.site.site_title = "Admin panel"
admin.site.index_title = "Tourastic"
