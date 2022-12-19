
import pytest
from django.test import TestCase
from django.urls import reverse
# Create your tests here.




@pytest.mark.django_db
def test_support(client):
   url = reverse('support')
   response = client.get(url)
   assert response.status_code == 201

