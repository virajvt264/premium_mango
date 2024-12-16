from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from home.views import *

urlpatterns = [
    path('index/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('track_order/', track_order, name='track_order'),
    path('shop_now/', shop_now, name='shop_now'),
    path('blog/', blog, name='blog'),
    # path('add_product/', add_product, name='add_product'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]