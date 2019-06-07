from datetime import date

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.CharField(max_length=150)
    date = models.DateField(default=date.today, editable=False)

    def __str__(self):
        return "{}'s order".format(self.customer)


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, related_name='ordered_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{} ({})".format(self.product, self.quantity)
