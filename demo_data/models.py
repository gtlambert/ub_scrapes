from django.db import models


class Category(models.Model):
    pk = models.IntegerField()


class Review(models.Model):
    pk = models.IntegerField()
    category = models.ForeignKey(Category)
