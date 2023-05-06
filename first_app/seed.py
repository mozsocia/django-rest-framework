import random
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import *

User = get_user_model()


def seed_data():

    # Create categories
    electronics = Category.objects.create(name='Electronics')
    clothing = Category.objects.create(name='Clothing')
    books = Category.objects.create(name='Books')
    beauty = Category.objects.create(name='Beauty')
    sports = Category.objects.create(name='Sports')
    contemporary = Category.objects.create(name='Contemporary')

    
    

    # Create products
    product1 = Product.objects.create(name='Macbook Pro', price=1500)
    product1.categories.set([electronics, beauty])
    product2 = Product.objects.create(name='iPhone 12', price=1000)
    product2.categories.set([electronics, contemporary])
    product3 = Product.objects.create(name='Samsung Galaxy S21', price=800)
    product3.categories.set([electronics, beauty])
    product4 = Product.objects.create(name='Fitbit Versa 3', price=200)
    product4.categories.set([electronics, sports])
    product5 = Product.objects.create(name='Sony WH-1000XM4', price=350)
    product5.categories.set([electronics, clothing])
    product6 = Product.objects.create(name='T-Shirt', price=20)
    product6.categories.set([clothing, electronics])
    product7 = Product.objects.create(name='Jeans', price=50)
    product7.categories.set([clothing, books])
    product8 = Product.objects.create(name='Dress', price=80)
    product8.categories.set([clothing, sports])
    product9 = Product.objects.create(name='Sneakers', price=100)
    product9.categories.set([clothing, sports])
    product10 = Product.objects.create(name='Running Shoes', price=120)
    product10.categories.set([clothing, sports])
    product11 = Product.objects.create(name='To Kill a Mockingbird', price=10)
    product11.categories.set([books, sports])
    product12 = Product.objects.create(name='The Catcher in the Rye', price=12)
    product12.categories.set([books, contemporary])
    product13 = Product.objects.create(name='Harry Potter and the Philosopher\'s Stone', price=15)
    product13.categories.set([books, contemporary])
    product14 = Product.objects.create(name='The Alchemist', price=8)
    product14.categories.set([books, sports])
    product15 = Product.objects.create(name='The Girl on the Train', price=7)
    product15.categories.set([books, contemporary])
