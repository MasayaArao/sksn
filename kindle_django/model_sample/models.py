from django.db import models

class Item(models.Model):
    namae = models.CharField(max_length=200)
    old = models.IntegerField(default=0)
    money = models.IntegerField(default=0)

    def __str__(self):
        return "id: %s namae: %s" %(self.id,self.namae)