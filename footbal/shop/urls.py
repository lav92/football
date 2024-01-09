from django.urls import path

from shop.views import (HomePage, GoodsByCategory, cart_add, show_cart, cart_decrease, cart_delete, clear_cart,
                        save_order, order_list)

app_name = 'shop'

urlpatterns = [
    # urls goods catalog
    path('', HomePage.as_view(), name='home'),
    path('category/<slug:cat_slug>/', GoodsByCategory.as_view(), name='goods_category'),
    # urls for cart
    path('cart/', show_cart, name='show_cart'),
    path('add/<slug:product_slug>/', cart_add, name='add-to-cart'),
    path('decrease/<slug:product_slug>/', cart_decrease, name='decrease'),
    path('remove/<slug:product_slug>/', cart_delete, name='remove'),
    path('clear/', clear_cart, name='clear'),
    # order url
    path('order/', save_order, name='order'),
    path('order_history/', order_list, name='order_history'),
]
