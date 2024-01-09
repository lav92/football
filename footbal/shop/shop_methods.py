from shop.models import Cart, Order


def create_goods_list(user) -> dict:
    goods_list = Cart.objects.filter(user=user)
    goods_dict = {}
    total_price = 0
    for goods in goods_list:
        product_id = goods.goods.pk
        goods_dict[str(product_id)] = {'name': goods.goods.name, 'price': str(goods.goods.price),
                                       'quantity': goods.quantity}
        total_price += goods.quantity * goods.goods.price
    goods_dict['total_price'] = str(total_price)
    goods_list.delete()
    return goods_dict


def parse_orders(user) -> list:
    order_querylist = Order.objects.filter(user=user).order_by('-created_at')
    order_sequence = []
    for order in order_querylist:
        order_sequence.append({'order_id': order.pk, 'date': order.created_at,
                               'total_price': order.goods_list['total_price'],
                               'product_list': [value for value in order.goods_list.values() if
                                                isinstance(value, dict)]})
    return order_sequence
