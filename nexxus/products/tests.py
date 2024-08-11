from django.test import TestCase  # type: ignore
from django.urls import reverse  # My Url

from .models import Product  # Model


class ProductListViewTest(TestCase):

    def test_should_return_200(self):
        url = reverse("list_product")  # Go back
        response = self.client.get(url)  # My Url
        # 200 => Sucess ?
        self.assertEqual(response.status_code, 200)  # Assert => Valid result
        self.assertEqual(response.context["products"].count(), 0)  # No new products

    def test_should_return_200_with_products(self):
        url = reverse("list_product")  # Go back
        Product.objects.create(  # Insert a Product
            name="test",
            description="test description",
            priceCost="5",
            priceSell="8",
            available=True,
            units="4",
        )
        response = self.client.get(url)  # My Url
        # 200 => Sucess ?
        self.assertEqual(response.status_code, 200)  # Assert => Valid result
        self.assertEqual(response.context["products"].count(), 1)  # A new product
