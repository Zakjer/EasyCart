import pytest
from rest_framework import status 
from model_bakery import baker

from shop.models import Product

@pytest.mark.django_db
class TestCreateProduct:
    """Tests for adding a product"""

    def test_if_user_is_not_admin_returns_403(self, api_client, authenticate):
        authenticate(is_staff=False)

        response = api_client.post('/shop/products/', {'title': 'a', 'description': 'a', 'price': 1})

        assert response.status_code == status.HTTP_403_FORBIDDEN 

    def test_if_user_is_admin_returns_201(self, api_client, authenticate):
        authenticate(is_staff=True)

        response = api_client.post('/shop/products/', {'title': 'a', 'description': 'a', 'price': 1})

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_valid_returns_201(self, api_client, authenticate):
        authenticate(is_staff=True)

        response = api_client.post('/shop/products/', {'title': 'a', 'description': 'a', 'price': 1})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

    def test_if_data_is_invalid_returns_400(self, api_client, authenticate):
        authenticate(is_staff=True)

        response = api_client.post('/shop/products/', {'title': '', 'description': '', 'price': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestRetrieveProduct:
    """Tests for retrieving a product"""

    def test_if_product_exists_returns_200(self, api_client):
        product = baker.make(Product)

        response = api_client.get(f'/shop/products/{product.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_product_not_exists_returns_404(self, api_client):
        non_existent_id = 9999

        response = api_client.get(f'/shop/products/{non_existent_id}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestModifyProduct:
    """Tests for modyfing a product"""

    def test_if_user_is_admin_returns_200(self, api_client, authenticate):
        authenticate(is_staff=True)
        product = baker.make(Product)

        response = api_client.patch(f'/shop/products/{product.id}/', {'title': 'a'})

        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_not_admin_returns_403(self, api_client, authenticate):
        authenticate(is_staff=False)
        product = baker.make(Product)

        response = api_client.patch(f'/shop/products/{product.id}/', {'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_returns_200(self, api_client, authenticate):
        authenticate(is_staff=True)
        product = baker.make(Product)

        response = api_client.patch(f'/shop/products/{product.id}/', {'title': 'a'})

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] > 0

    def test_if_data_is_invalid_returns_400(self, api_client, authenticate):
        authenticate(is_staff=True)
        product = baker.make(Product)

        response = api_client.patch(f'/shop/products/{product.id}/', {'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestDeleteProduct:
    """Tests for deleting a product"""

    def test_if_user_is_admin_returns_204(self, api_client, authenticate):
        authenticate(is_staff=True)
        product = baker.make(Product)

        response = api_client.delete(f'/shop/products/{product.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_user_is_not_admin_returns_403(self, api_client, authenticate):
        authenticate(is_staff=False)
        product = baker.make(Product)

        response = api_client.delete(f'/shop/products/{product.id}/')

        response.status_code == status.HTTP_403_FORBIDDEN



        
