from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    def __str__(self):
        return self.title

class Chocolate(models.Model):
    title=models.CharField(max_length=200)
    category = models.ForeignKey(Category,related_name='chocolates',on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True,blank=True)
    image_url = models.URLField(max_length=2083)
    choco_available=models.BooleanField()
    is_deleted =models.BooleanField()

    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.name

class Cart(models.Model):
    items = models.ManyToManyField(Chocolate)

class Favorite(models.Model):
    items = models.ManyToManyField(Chocolate)