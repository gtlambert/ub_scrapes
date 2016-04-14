from django.db import models


class Category(models.Model):
    num = models.IntegerField()


class Review(models.Model):
    num = models.IntegerField()
    category = models.ForeignKey(Category)
