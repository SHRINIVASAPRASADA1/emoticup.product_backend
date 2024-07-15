from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    discount = models.DecimalField(blank=True,null=True,max_digits=6,decimal_places=0)
    image = models.JSONField(blank=True,null=True)
    ratting = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now=True,blank=True,null=True)
    quantity = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
