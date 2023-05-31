from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the NFTeria index.")


def about(request):
    return render(request, "about.html")


def marketplace(request):
    return render(request, "marketplace.html")


def contact(request):
    return render(request, "contact.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def profile(request):
    return render(request, "profile.html")


def create(request):
    return render(request, "create.html")


def edit(request):
    return render(request, "edit.html")


def delete(request):
    return render(request, "delete.html")


def view(request):
    return render(request, "view.html")


def search(request):
    return render(request, "search.html")


def buy(request):
    return render(request, "buy.html")


def sell(request):
    return render(request, "sell.html")


def bid(request):
    return render(request, "bid.html")


def auction(request):
    return render(request, "auction.html")


def settings(request):
    return render(request, "settings.html")


def terms(request):
    return render(request, "terms.html")


def privacy(request):
    return render(request, "privacy.html")


def faq(request):
    return render(request, "faq.html")


def help(request):
    return render(request, "help.html")


def support(request):
    return render(request, "support.html")


# this makes it so that you can use the url tag in your templates. modularity!
"""
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class MarketplaceView(TemplateView):
    template_name = "marketplace.html"

# ... define the rest of your views

"""
