from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to="files")

class Candle(models.Model):
    id = models.IntegerField(primary_key=True)
    open = models.DecimalField(max_digits=5, decimal_places=2)
    high = models.DecimalField(max_digits=5, decimal_places=2)
    low = models.DecimalField(max_digits=5, decimal_places=2)
    close = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()   