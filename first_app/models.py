from django.db import models

# Create your models here.


# class Person(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField()

#     def __str__(self):
#         return self.first_name + " " + self.last_name


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Book(models.Model):
#     book_title = models.CharField(max_length=100)
#     category = models.ForeignKey(
#         Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.book_title


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)

