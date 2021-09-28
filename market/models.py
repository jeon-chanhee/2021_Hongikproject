from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from accounts.models import Profile


class Store(models.Model):
    name = models.CharField(max_length=30, db_column='store_name')
    tel = models.CharField(max_length=11, db_column='store_tel')
    opentime = models.CharField(max_length=20, db_column='store_open')
    closetime = models.CharField(max_length=20, db_column='store_close')

    class Meta:
        db_table = 'store'

    def __str__(self):
        return self.name


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_column='product_name')
    intro = models.TextField(db_column='product_intro')
    weight = models.CharField(max_length=10, db_column='product_weight')
    origin = models.CharField(max_length=20, db_column='product_origin')
    photo = models.ImageField(db_column='product_photo')
    price = models.PositiveIntegerField(db_column='product_price')
    stock = models.PositiveIntegerField(db_column='product_stock')

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name



class Recommendation(models.Model):
    person = models.IntegerField(db_column='recom_user')
    sex = models.CharField(max_length=2, db_column='recom_sex')
    age = models.CharField(max_length=3, db_column='recom_age')
    job = models.CharField(max_length=30, db_column='recom_job')
    family_amount = models.CharField(
        max_length=10, db_column='recom_family_amount')
    food1 = models.CharField(max_length=30, db_column='recom_food1')
    food2 = models.CharField(max_length=30, db_column='recom_food2')
    food3 = models.CharField(max_length=30, db_column='recom_food3')
    item1 = models.CharField(max_length=30, db_column='recom_item1')
    item2 = models.CharField(max_length=30, db_column='recom_item2')
    item3 = models.CharField(max_length=30, db_column='recom_item3')
    mbti = models.CharField(max_length=4, db_column='recom_mbti')

    class Meta:
        db_table = 'recommendation'

   
