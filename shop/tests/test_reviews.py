from urllib import response
import pytest
from rest_framework import status
from model_bakery import baker

from shop.models import Product, Review

@pytest.mark.django_db
class TestRetrieveReview:
    """Tests for retrieving review"""

    def test_retrieve_review_returns_200(self, api_client):
        product = baker.make(Product)

        response = api_client.get(f'/shop/products/{product.id}/reviews/')

        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestCreateReview:
    """Tests for creating review"""

    def test_if_user_is_not_admin_returns_201(self, api_client, authenticate):
        authenticate(is_staff=False)
        product = baker.make(Product)

        response = api_client.post(f'/shop/products/{product.id}/reviews/', {'stars': 1, 'text': 'a'})

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_user_is_anpnymus_returns_403(self, api_client):
        product = baker.make(Product)

        response = api_client.post(f'/shop/products/{product.id}/reviews/', {'stars': 1, 'text': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_returns_201(self, api_client, authenticate):
        authenticate(is_staff=True)
        product = baker.make(Product)

        response = api_client.post(f'/shop/products/{product.id}/reviews/', {'stars': 1, 'text': 'a'})

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_returns_400(self, api_client, authenticate):
        authenticate(is_staff=True)
        product = baker.make(Product)

        #Max number of stars is 5
        response = api_client.post(f'/shop/products/{product.id}/reviews/', {'stars': 6, 'text': 'a'})

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestDeleteReview:
    """Tests for deleting review"""

    def test_if_user_is_admin_returns_204(self, api_client, authenticate):
        authenticate(is_staff=True)
        product = baker.make(Product)
        review = baker.make(Review)

        response = api_client.delete(f'/shop/products/{product.id}/reviews/{review.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_user_is_not_admin_returns_403(self, api_client, authenticate):
        authenticate(is_staff=False)
        product = baker.make(Product)
        review = baker.make(Review)

        response = api_client.delete(f'/shop/products/{product.id}/reviews/{review.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN
    
