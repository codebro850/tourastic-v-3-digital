from django.contrib import admin
from django.urls import path
from holidays import views
from django.contrib.auth import views as auth_views  # import this
urlpatterns = [
    path('', views.index, name="home"),
    path("st_tour/<package_name>/", views.packageinfo, name="packageinfo"),
    path("contact-us/", views.contactpage, name="contactpage"),
    path("category/blog/", views.blog, name="blogs"),
    path("tourpackages/", views.tours, name="tours"),
    path("destination/<destination_name>", views.destination, name="blogs"),
    path('update_item/', views.updateItem, name="update_item"),
    path('login/', views.logins, name="login"),
    path('logout/', views.logouts, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('cart/', views.cart, name="cart"),
    path("password_reset_request/", views.password_reset_request,
         name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('messagesend/', views.messagesend, name="messagesend"),
    path('confirm_order/<package_title>',
         views.create_order, name='create_order'),
    path('payment_status',  views.payment_status, name='payment_status'),
    path('book/<package_title>', views.book, name="book"),
    # path('login/',views.logins,name='login')
    path('order-history/', views.history, name="history"),
    path('saved/', views.saved, name="saved"),
    path("promo-check/", views.promo, name="promo"),
    path("address-save/", views.addresssave, name="addresssave"),
    path("username-check/", views.usernamecheck, name="usernamecheck"),
    path("email-check/", views.emailcheck, name="emailcheck"),
    path("search/", views.searchdestiny, name="searchdestiny"),
    path('changecurr/', views.postingcurr, name="changingcurrrency"),
    path("details/<package_title>/",
         views.detailform, name="detailform"),
    path("blog/<blogname>/", views.blogshow, name="blogshow"),
    path("passengerdetail/<pack>", views.savingdat, name="savingdata"),
]
