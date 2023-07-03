from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task(5)
    def view_products(self):
        self.client.get(f'/shop/products', name='/shop/products')

    @task(2)
    def view_product(self):
        product_id = randint(1, 1000)
        self.client.get(f'/shop/products/{product_id}', name='/shop/products/:id')