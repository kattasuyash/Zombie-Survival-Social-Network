from django.db import models

# Create your models here.
class Survivors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=155)
    age = models.IntegerField()
    gender = models.CharField(max_length=7)
    latitude = models.DecimalField(max_digits=6, decimal_places=2)
    longitude = models.DecimalField(max_digits=6, decimal_places=2)
    infected = models.BooleanField(null=False)

    def __str__(self):
        return self.name