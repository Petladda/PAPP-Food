from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    special_price = models.IntegerField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    image = models.ImageField(upload_to="foodsImage", blank=True)
    def __str__(self):
        return self.name