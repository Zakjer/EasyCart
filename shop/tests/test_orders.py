import pytest
from model_bakery import baker
from rest_framework import status

from shop.models import Order

@pytest.mark.django_db
class TestRetrieveOrder:
    """Testf for retrieving an order"""

    def if_user_is_admin_returns_200(self, api_client, authenticate):
        authenticate(is_staff=True)
        order = baker.make(Order)

        response = api_client.get(f'/store/orders/{order.id}/')

        assert response.status_code == status.HTTP_200_OK