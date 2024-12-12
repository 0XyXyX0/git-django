from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from shop.models import Tag, Item, Category, Image, ItemManager
from faker import Faker
from django.db import transaction
import time

faker = Faker()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # category = Category(name='toys', description='about toys')
        # category.save()
        # print(category.id)

        # category = Category.objects.create(name='cars')
        # print(category.id)





        # start = time.time()
        # for _ in range(1000):
        #     category = Category(name=faker.word())
        #     category.save()
        # end = time.time()
        # print(end-start)

        # start = time.time()
        # categories = []
        # for _ in range(1000):
        #     category = Category(name=faker.word())
        #     categories.append(category)
        # Category.objects.bulk_create(categories)
        # end = time.time()
        # print(end-start)




    
        # categories = Category.objects.filter(id__gt=500)
        # to_update = []

        # for category in categories:
        #     category.name = faker.word()
        #     to_update.append(category)

        # Category.objects.bulk_update(to_update, fields=['name'])





        # Category.objects.filter(id__gt=500).delete()




        # with transaction.atomic():
        category = Category.objects.create(name='For blacks')
        item = Item.objects.create(name='KFC', category=category)