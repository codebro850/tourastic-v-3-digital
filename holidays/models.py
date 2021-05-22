from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class routines(models.Model):
    day1 = models.TextField(blank=True)
    day2 = models.TextField(blank=True)
    day4 = models.TextField(blank=True)
    day3 = models.TextField(blank=True)
    day5 = models.TextField(blank=True)
    day6 = models.TextField(blank=True)
    day7 = models.TextField(blank=True)
    day8 = models.TextField(blank=True)
    day9 = models.TextField(blank=True)
    day_10 = models.TextField(blank=True)
    day_11 = models.TextField(blank=True)
    day_12 = models.TextField(blank=True)
    day_13 = models.TextField(blank=True)

    def __str__(self):
        return self.day1


class package_servicess(models.Model):
    service = models.CharField(max_length=200, default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service


class packages(models.Model):
    package_id = models.AutoField
    package_country = models.CharField(max_length=100, default="")
    package_city = models.CharField(max_length=100, default="", blank=True)
    package_title = models.CharField(max_length=100, default="")
    package_desc = models.TextField(default="")
    package_routine = models.ForeignKey(
        routines, on_delete=models.SET_NULL, null=True)
    package_type = models.CharField(max_length=50, default="")
    package_images = models.ImageField(
        upload_to="holidays/package_image", default="")
    package_categories = models.CharField(max_length=50, default="")
    package_duration = models.IntegerField(default=0)
    package_price = models.DecimalField(max_digits=20, decimal_places=2)
    package_hotels = models.TextField(default="")
    package_created = models.DateTimeField(default=timezone.now())
    package_createdby = models.CharField(max_length=50, default="")
    package_restaurant = models.TextField(default="")
    package_food = models.TextField(default="")
    package_group_size = models.CharField(
        max_length=100, default="unlimited", blank=True)
    package_service = models.ManyToManyField(package_servicess)
    package_pickup = models.TextField(default="")
    package_drop = models.TextField(default="")
    package_video = models.FileField(
        upload_to="holidays/package_videos", default="")

    def __str__(self):
        return self.package_title


class order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(default=timezone.now())
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, default="", blank=True)
    order_id = models.CharField(max_length=100, default="", blank=True)
    amout_paid = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0.00)
    package = models.ForeignKey(packages, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.customer)

    @property
    def get_cart_total(self):
        orderitems = self.orderforpackage_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderforpackage_set.all()
        total = orderitems.count()
        return total


class orderforpackage(models.Model):
    order_id = models.AutoField
    order = models.ForeignKey(order, on_delete=models.SET_NULL, null=True)
    package = models.ForeignKey(packages, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=50, default="")
    passengers = models.IntegerField(default=0, blank=True)
    child = models.IntegerField(default=0, blank=True)
    infants = models.IntegerField(default=0, blank=True)
    daya_tour = models.IntegerField(default=0, blank=True)
    date_tour = models.DateField(blank=True, null=True)
    enddate_tour = models.DateField(blank=True, null=True)
    order_status = models.CharField(max_length=50, default="", blank=True)
    price_package = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True)
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00, blank=True)
    date_ordered = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.username

    @property
    def get_total(self):
        total = float(self.price_package*(int(self.passengers)) +
                      (self.price_package/2)*(int(self.child)))
        return total


class offers(models.Model):
    package = models.ForeignKey(packages, on_delete=models.SET_NULL, null=True)
    offer = models.BooleanField(default=False)
    discount_percentage = models.IntegerField(default=0, blank=True)
    valid_to = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(default=timezone.now())
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.offer)


# customize oder will be created after words
class hotels(models.Model):
    hotels_id = models.AutoField
    hotel_city = models.CharField(max_length=50, default="")
    hotel_country = models.CharField(max_length=100, default="")
    hotel_name = models.CharField(max_length=50, default="")
    hotel_image = models.ImageField(upload_to="holidays/pro_image", default="")
    hotel_description = models.TextField(default="")
    hotel_services = models.TextField(default="")
    hotels_price = models.DecimalField(max_digits=20, decimal_places=2)
    hotel_createdby = models.CharField(max_length=50, default="")
    hotel_no_of_rooms = models.IntegerField(default=0)
    hotel_type_room = models.CharField(max_length=20, default="")
    datetime = models.DateTimeField(default=datetime.now())
    hotel_updatedon = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.hotels_id


class transport(models.Model):
    transport_id = models.AutoField
    transport_mode = models.CharField(max_length=50, default="")
    service_name = models.CharField(max_length=100, default="")
    price_per_km = models.DecimalField(max_digits=20, decimal_places=2)
    added_by = models.CharField(max_length=50, default="")
    company_name = models.CharField(max_length=100, default="")
    datetime = models.DateTimeField(default=timezone.now())

# class food(models.Model):
#     food_id=models.AutoField
#     restaurant_name=models.CharField(max_length=100,default="")
#     food_desc=models.TextField


class userinfo(models.Model):
    users = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.TextField(default="")
    mobile_no = models.IntegerField(default=0)
    pincode = models.IntegerField(max_length=5, default=0)
    country = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=100, default="")
    datetime = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.address


class blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, default="")
    images = models.ImageField(upload_to="holidays/pro_image", default="")
    description = models.TextField()
    createdat = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class bloginfo(models.Model):
    blog = models.ForeignKey(blogs, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    timeupdated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog.title


class comments(models.Model):
    blog = models.ForeignKey(blogs, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100, default="")
    commented_on = models.DateTimeField(default=timezone.now())
    comment = models.TextField()

    def __str__(self):
        return self.comment


class affiliateaccounts(models.Model):
    username = models.CharField(max_length=50, default="", unique=True)
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=100, default="")
    date_joined = models.DateTimeField(default=timezone.now())
    aid = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class affiliateinfo(models.Model):
    affiliate_user = models.ForeignKey(
        affiliateaccounts, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100, default="")
    second_name = models.CharField(max_length=100, default="", blank=True)
    mobile_number = models.IntegerField(max_length=12, default=0)
    pincode = models.IntegerField(max_length=8, default=0)
    state = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    country = models.CharField(max_length=100, default="")
    address_temp = models.CharField(max_length=200, default="", blank=True)
    date_edited = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.affiliate_user)


class banner(models.Model):
    banner_image = models.ImageField(
        upload_to="holidays/pro_image", default="")
    url = models.CharField(max_length=100, default="")
    datecreated = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.url


class reviews(models.Model):
    star = models.IntegerField(default=0)
    packages = models.ForeignKey(
        packages, on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    datecreated = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.star)


class destinations(models.Model):
    image = models.ImageField(
        upload_to="holidays/destination_image", default="")
    video = models.FileField(
        upload_to="holidays/destination_video", default="")
    name = models.CharField(max_length=100, default="")
    description = models.TextField(blank=True)
    timecreated = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class services(models.Model):
    image = models.ImageField(upload_to="holidays/services_image", default="")
    title = models.CharField(max_length=200, default="")
    desc = models.TextField(default="")
    time_created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class promocode(models.Model):
    promo_code = models.CharField(max_length=100, unique=True, default="")
    discount_percentage = models.DecimalField(decimal_places=2, max_digits=20)
    term_condition = models.TextField(default="")
    used_by_specific_user = models.BooleanField(default=False)
    used_for_all = models.BooleanField(default=False)
    user_for_promocode = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.CharField(default="", max_length=100)
    time_created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.promo_code


class promo_used(models.Model):
    user_used = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    promocode = models.ForeignKey(
        promocode, on_delete=models.SET_NULL, null=True)
    package = models.ForeignKey(
        packages, on_delete=models.SET_NULL, null=True, blank=True)
    used_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_used.username


class promo_process(models.Model):
    promo_cod = models.ForeignKey(
        promocode, on_delete=models.SET_NULL, null=True)
    users = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100, default="", blank=True)
    package = models.ForeignKey(
        packages, on_delete=models.SET_NULL, null=True, blank=True)
    promo_added = models.DateTimeField(auto_now_add=True)
    price_package = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.users.username


class affiliate_success(models.Model):
    affiliateuser = models.ForeignKey(
        affiliateaccounts, on_delete=models.SET_NULL, null=True)
    successful_affiliate = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    affiliate_product = models.ForeignKey(
        packages, on_delete=models.SET_NULL, null=True, blank=True)
    ammount_received = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True)
    ammount_earned_affiliate = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    percentage_affiliate = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, default=0)
    date_affiliate_successfull = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.affiliateuser.username


class affialiate_click(models.Model):
    affliateuser = models.ForeignKey(
        affiliateaccounts, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    date_logged_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.affliateuser.username


class affiliate_info_user(models.Model):
    affliateuser = models.ForeignKey(
        affiliateaccounts, on_delete=models.SET_NULL, null=True)
    visited = models.IntegerField(default=0)
    logged_in_users = models.IntegerField(default=0)
    successfull_affiliate = models.IntegerField(default=0)
    ammount_received = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    ammount_withdrawn = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, blank=True)
    updated_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.affliateuser.username


class affiliate_transaction(models.Model):
    affliateuser = models.ForeignKey(
        affiliateaccounts, on_delete=models.SET_NULL, null=True)
    ammount_withdrawn = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    ammount_left = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    transaction_id = models.CharField(max_length=100, default="")
    date_of_transaction = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.affliateuser.username


class trendingtours(models.Model):
    package = models.ForeignKey(packages, on_delete=models.SET_NULL, null=True)
    useradded = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    datetimecreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.useradded.username


class messagess(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=80, default="")
    subject = models.CharField(max_length=200, default="")
    messages = models.TextField()
    messaged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class testimonial(models.Model):
    name = models.CharField(max_length=100, default="")
    testi_image = models.ImageField(
        upload_to="holidays/testimonials", default="")
    profession = models.CharField(max_length=100, default="", blank=True)
    review = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class teammembers(models.Model):
    name = models.CharField(max_length=100, default="")
    profile_image = models.ImageField(upload_to="holidays/members", default="")
    position = models.CharField(max_length=100, default="")
    social_fb = models.CharField(max_length=200, default="", blank=True)
    social_insta = models.CharField(max_length=200, default="", blank=True)
    social_twitter = models.CharField(max_length=200, default="", blank=True)
    social_google = models.CharField(max_length=200, default="", blank=True)
    social_linkln = models.CharField(max_length=200, default="", blank=True)
    social_snap = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.name


class passengers(models.Model):
    pas = models.CharField(max_length=100, default="", blank=True)
    age = models.IntegerField(default=0, blank=True)
    gender = models.CharField(max_length=50, default="")
    booked = models.DateTimeField(auto_now_add=True)
    pass_type = models.CharField(max_length=100, default="")
    package = models.ForeignKey(packages, on_delete=models.SET_NULL, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pas


class passengers_details(models.Model):
    passenger = models.ManyToManyField(passengers)
    orders = models.ForeignKey(order, on_delete=models.SET_NULL, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.orders.package.package_title
