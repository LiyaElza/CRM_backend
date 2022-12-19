from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import orders

# class TestMonthlySales(APITestCase):

#     def setUp(self):
#         super(TestMonthlySales, self).setUp()
#         self.authenticate()

#         def test_monthly_sales(self):
#             response = self.client.get('/monthlysales/')
#             print("response", response.status_code)
#             self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TestMonthlySales(APITestCase):
    def setUp(self):
        super(TestMonthlySales, self).setUp()
        self.test_monthly_sales()

    def test_monthly_sales(self):
        url = reverse('monthlysales')
        response = self.client.get(url)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)