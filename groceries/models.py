from django.db import models

class Unit(models.Model):
    unit_text = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.unit_text


class Item(models.Model):
    item_text = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)
    added_date = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return self.item_text



class Vendor(models.Model):
    vendor_text = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.vendor_text


class Buy(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,default=None )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)
    barcode = models.IntegerField(default=1)
    quantity = models.IntegerField()
    cost = models.IntegerField()
    buy_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.item.item_text + ":" + self.unit.unit_text + "-" + str(self.quantity) 
