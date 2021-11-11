import datetime
import uuid

from django.db import models


class Size(models.Model):
    size = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.size


class Cover(models.Model):
    cover = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.cover


class Page(models.Model):
    page = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.page


class Pattern(models.Model):
    pattern = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.pattern


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    # avatar = models.ImageField('Avatar', upload_to='uploads/', null=True)


    def __str__(self):
        return self.name


class Order(models.Model):
    size = models.ForeignKey('Size', default=1, on_delete=models.PROTECT)
    cover = models.ForeignKey('Cover', default=1, on_delete=models.PROTECT)
    pagesCount = models.IntegerField()
    pagesType = models.ForeignKey('Page', default=1, on_delete=models.PROTECT)
    pattern = models.ForeignKey('Pattern', default=1, on_delete=models.PROTECT)
    buyer = models.ForeignKey('Buyer', default=1, on_delete=models.PROTECT)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.number


class Review(models.Model):
    buyer = models.ForeignKey('Buyer', on_delete=models.PROTECT)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
