from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category', verbose_name='Категория')
    name = models.CharField(max_length=200, verbose_name='Под категория')

    def __str__(self):
        return f"{self.category.name} -- {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')

    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, related_name='sub_category')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    novelties = models.BooleanField(default=False, verbose_name='новинки')
    recommended = models.BooleanField(default=False, verbose_name='рекомендуемые')
    bestseller = models.BooleanField(default=False, verbose_name='хит продаж')
    in_stock = models.BooleanField(default=False, verbose_name='В наличии')

    def __str__(self):
        return f"{self.name}--{self.category.name}"

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/image/', verbose_name='Фотографии')

class Characteristics(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics')
    left_side = models.CharField(max_length=200, verbose_name='Левая сторона')
    right_side = models.CharField(max_length=200, verbose_name='Правая сторона')
