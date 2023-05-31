from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("marketplace/", views.marketplace, name="marketplace"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("create/", views.create, name="create"),
    path("edit/", views.edit, name="edit"),
    path("delete/", views.delete, name="delete"),
    path("view/", views.view, name="view"),
    path("search/", views.search, name="search"),
    path("buy/", views.buy, name="buy"),
    path("sell/", views.sell, name="sell"),
    path("bid/", views.bid, name="bid"),
    path("auction/", views.auction, name="auction"),
    path("settings/", views.settings, name="settings"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("faq/", views.faq, name="faq"),
    path("help/", views.help, name="help"),
    path("support/", views.support, name="support"),
]


# this makes it so that you can use the url tag in your templates. modularity!
"""
from django.urls import path
from .views import IndexView, AboutView, MarketplaceView  #... import the rest of your views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("marketplace/", MarketplaceView.as_view(), name="marketplace"),
    # ... repeat for the rest of your views
]


"""
