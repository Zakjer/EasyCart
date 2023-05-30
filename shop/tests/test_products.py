import pytest
from rest_framework import status 

class TestCreateProduct:
    """Tests for adding a product"""

    def test_if_user_is_not_admin_returns_403(self, api_client, authenticate):
        authenticate(is_staff=False)

        response = api_client.post('/shop/products/', {'title': 'a', 'description': 'a', 'price': 1})

        assert response.status_code == status.HTTP_403_FORBIDDEN 
