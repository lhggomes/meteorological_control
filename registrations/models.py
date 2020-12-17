from django.db import models


class Target(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    exp_date = models.DateField()

    def __str__(self):
        return f'{self.name} -  @{self.longitude}, {self.latitude}z'



