from django.test import TestCase

import pytest

from django.urls import reverse

testinput=[{""},{}]

@pytest.mark.django_db
@pytest.mark.parametrize('testinput',testinput)

def test_languages(product_type,product,message,client):
   url = reverse('offer')
   response = client.get(
       url, data={'product_type': product_type,'product':product,'message':message}
   )
   assert response.status_code == 201
