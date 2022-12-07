from django.test import TestCase

import pytest

from django.urls import reverse

testinput=[{"product_type":"Cosmetics","product":"Powder","message":"Buy 1 Get 1 free"},{"product_type":"Gadgets","Laptop":"Powder","message":"Buy 1 Get 1 free"}]

@pytest.mark.django_db
@pytest.mark.parametrize('testinput',testinput)

def test_languages(testinput,client):
   url = reverse('offer')
   response = client.get(
       url, data=testinput
   )
   assert response.status_code == 400
