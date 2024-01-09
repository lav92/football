from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from shop.models import Goods, Category, Cart, Order
from shop.forms import OrderForm
from shop.shop_methods import create_goods_list, parse_orders


class HomePage(ListView):
    Model = Goods
    template_name = 'shop/home.html'
    context_object_name = 'product'
    paginate_by = 6
    extra_context = {
        'title': 'All Goods',
    }

    def get_queryset(self):
        return Goods.objects.all()


class GoodsByCategory(ListView):
    Model = Goods
    template_name = 'shop/home.html'
    context_object_name = 'product'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['title'] = cat.name
        return context

    def get_queryset(self):
        return Goods.objects.filter(category__slug=self.kwargs['cat_slug'])


def cart_add(request, product_slug):
    product = Goods.objects.get(slug=product_slug)

    cart = Cart.objects.filter(user=request.user, goods=product)
    if cart.exists():
        cart = cart.first()
        cart.quantity += 1
        cart.save()
    else:
        Cart.objects.create(user=request.user, goods=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])


def cart_decrease(request, product_slug):
    product = Goods.objects.get(slug=product_slug)

    cart = Cart.objects.filter(user=request.user, goods=product)
    if cart.exists():
        cart = cart.first()
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
    return redirect(request.META['HTTP_REFERER'])


def cart_delete(request, product_slug):
    product = Cart.objects.get(user=request.user, goods__slug=product_slug)
    product.delete()
    return redirect(request.META['HTTP_REFERER'])


def clear_cart(request):
    product_querry = Cart.objects.filter(user=request.user)
    for product in product_querry:
        product.delete()
    return redirect(reverse('shop:home'))


def show_cart(request):
    cart = Cart.objects.filter(user=request.user)
    total = round(sum(cart.quantity * cart.goods.price for cart in cart), 2)
    context = {
        'cart': cart,
        'total': total
    }
    return render(request, 'shop/cart.html', context)


def save_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            client = request.user
            try:
                Order.objects.create(user=request.user, phone=form.cleaned_data['phone'],
                                     address=form.cleaned_data['address'],
                                     delivery_date=form.cleaned_data['delivery_date'],
                                     goods_list=create_goods_list(client))
            except Exception as e:
                print(e)
            return redirect(reverse('shop:home'))
    else:
        form = OrderForm()
    return render(request, 'shop/order-page.html', {'form': form})


def order_list(request):
    client = request.user
    return render(request, 'shop/order-list.html', context={'orders': parse_orders(client)})
