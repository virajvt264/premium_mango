from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Cart, CartItem

class CartTests(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create products
        self.product1 = Product.objects.create(name="Apple", price=1.50, stock=100)
        self.product2 = Product.objects.create(name="Banana", price=0.80, stock=200)

    def test_add_to_cart(self):
        # Log in the user
        self.client.login(username='testuser', password='password')

        # Add product to the cart
        response = self.client.post(f'/add-to-cart/{self.product1.id}/')
        self.assertEqual(response.status_code, 302)  # Redirect after adding

        # Verify the product is in the cart
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 1)
        cart_item = cart.items.first()
        self.assertEqual(cart_item.product, self.product1)
        self.assertEqual(cart_item.quantity, 1)

    def test_update_quantity(self):
        # Log in and add product
        self.client.login(username='testuser', password='password')
        self.client.post(f'/add-to-cart/{self.product1.id}/')
        self.client.post(f'/add-to-cart/{self.product1.id}/')  # Add again

        # Verify quantity is updated
        cart = Cart.objects.get(user=self.user)
        cart_item = cart.items.first()
        self.assertEqual(cart_item.quantity, 2)

    def test_remove_from_cart(self):
        # Log in and add product
        self.client.login(username='testuser', password='password')
        self.client.post(f'/add-to-cart/{self.product1.id}/')

        # Remove the product
        cart = Cart.objects.get(user=self.user)
        cart_item = cart.items.first()
        response = self.client.post(f'/remove-from-cart/{cart_item.id}/')
        self.assertEqual(response.status_code, 302)  # Redirect after removal

        # Verify cart is empty
        self.assertEqual(cart.items.count(), 0)
