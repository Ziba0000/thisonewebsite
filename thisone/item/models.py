from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category Name")

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    price = models.FloatField(verbose_name="Price")
    image = models.ImageField(upload_to='item_images', blank=True, null=True, verbose_name="Image")
    is_sold = models.BooleanField(default=False, verbose_name="Is Sold")
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE, verbose_name="Created By")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.name

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Item")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")

    def __str__(self):
        return f'{self.quantity} x {self.item.name}'
