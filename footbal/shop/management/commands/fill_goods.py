import random

from django.core.management import BaseCommand
from random import randint

from shop.models import Goods

FIELDS_DICT = {
    'name': 'Product',
    'slug': 'product_',
    'description': 'It is a long established fact that a reader will be distracted by the readable content of a page '
                   'when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal '
                   'distribution of letters, as opposed to using , making it look like readable English.',
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Заполним каталог товаров')
        for i in range(1, 100):
            goods = Goods.objects.create(name=f'{FIELDS_DICT["name"]} {i}',
                                         slug=f'{FIELDS_DICT["slug"]}{i}',
                                         description=FIELDS_DICT['description'],
                                         price=random.uniform(20.00, 100.00),
                                         stock=randint(1, 100),
                                         category_id=randint(1, 4),
                                         )
            self.stdout.write(f'created {goods.name}')
            goods.save()

            self.stdout.write(f'Товар {goods.name} создан')
        self.stdout.write('Done')
