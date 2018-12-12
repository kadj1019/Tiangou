from django.db import models


class Brand(models.Model):
    img = models.CharField(max_length=100)


class Computer1(models.Model):
    img = models.CharField(max_length=100)


class Computer_list(models.Model):
    img = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)
    price = models.CharField(max_length=100)


class Computer_lun(models.Model):
    img = models.CharField(max_length=100)


class Dress_list(models.Model):
    img = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)
    price = models.CharField(max_length=100)


class Dress_lun(models.Model):
    img = models.CharField(max_length=100)


class Gift_lun(models.Model):
    img = models.CharField(max_length=100)


class Goods(models.Model):
    img = models.CharField(max_length=100)
    bianHao = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    shopPrice = models.CharField(max_length=100)
    jieShao = models.CharField(max_length=100)


class Lunbo(models.Model):
    img = models.CharField(max_length=100)


class Makeup_list(models.Model):
    img = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)
    price = models.CharField(max_length=100)


class Makeup_lun(models.Model):
    img = models.CharField(max_length=100)


class Phone_list(models.Model):
    img = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)
    price = models.CharField(max_length=100)


class Phone_lun(models.Model):
    img = models.CharField(max_length=100)


class Vip(models.Model):
    img = models.CharField(max_length=100)


class Product1(models.Model):
    img = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

class User(models.Model):
    email = models.CharField(max_length=40, unique=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=256)
    token = models.CharField(max_length=256,default=1)

    class Meta:
        db_table = 'app_user'