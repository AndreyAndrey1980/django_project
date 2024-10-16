from django.shortcuts import render
from .models import Product, Category
from django.http import Http404


def index(request):
    products = Product.objects.all()
    return render(request, "catalog/index.html", {"products": products})


def get_contact_info(request):
    return render(request, "catalog/contact_info.html", {})


def detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    context = {"product": product}
    return render(request, "catalog/detail.html", context)
