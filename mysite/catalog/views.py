from django.shortcuts import render


def index(request):
    # работа с бд и подготовка информации
    products_from_db = ['potato', 'apple', 'cucumber']
    return render(request, "catalog/index.html", {"products": products_from_db})


def get_contact_info(request):
    return render(request, "catalog/contact_info.html", {})
