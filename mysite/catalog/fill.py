from django.core.management import BaseCommand
import json
from .models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_catalog():
    # Здесь мы получаем данные из фикстурв с категориями
        with open("catalog/catalog_data.json") as f:
            return json.load(f)

    def handle(self, *args, **options):
        categories_and_products = Command.json_read_catalog()
        product_for_create = []
        category_for_create = []

        for category in [x for x in categories_and_products if x["model"] == "catalog.category"]:
            category_for_create.append(
                Category(category["pk"], category["fields"]["name"], category["fields"]["description"])
            )

        Category.objects.bulk_create(category_for_create)
        for product in [x for x in categories_and_products if x["model"] == "catalog.product"]:
            product_for_create.append(
                Product(product["pk"],
                        product["fields"]["name"],
                        product["fields"]["description"],
                        product["fields"]["category"],
                        product["fields"]["price"],
                        product["fields"]["create_date"],
                        product["fields"]["last_change_date"],
                        product["fields"]["image"]))

        Product.objects.bulk_create(product_for_create)
