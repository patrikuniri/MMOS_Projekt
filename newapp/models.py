from django.db import models

class VanbrodskiMotori(models.Model):
    marka = models.CharField(max_length=100)
    jacina = models.IntegerField()
    price = models.IntegerField()
