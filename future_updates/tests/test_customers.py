import pytest
from rest_framework import status
from model_bakery import baker

from shop.models import Customer

@pytest.mark.django_db
class TestRetrieveCustomer:
    """Tests for retrieving a customer"""

    def test_if_user_is_admin_returns_200(self, api_client, authenticate):
        authenticate(is_staff=True)
        customer = baker.make(Customer)

        response = api_client.get(f'/shop/customers/{customer.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_not_admin_returns_403(self, api_client, authenticate):
        authenticate(is_staff=False)
        customer = baker.make(Customer)

        response = api_client.get(f'/shop/customers/{customer.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
class TestDeleteCustomer:
    """Tests for deleting a customer"""

    def test_if_user_is_admin_returns_204(self, api_client, authenticate):
        authenticate(is_staff=True)
        customer = baker.make(Customer)

        response = api_client.delete(f'/shop/customers/{customer.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_user_is_not_admin_returns_403(self, api_client, authenticate):
        authenticate(is_staff=False)
        customer = baker.make(Customer)

        response = api_client.delete(f'/shop/customers/{customer.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

