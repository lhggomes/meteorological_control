from django.db import models


class Target(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    exp_date = models.DateField()

    def __str__(self):
        return f'{self.name} -  @{self.longitude}, {self.latitude}z'


# Relationship 1-N
class Map(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Target)


# Relationship N-N
class Address(models.Model):
    name = models.CharField(max_length=200)
    maps = models.ManyToManyField(Map)


# Relationship 1-1
class Person(models.Model):
    name = models.CharField(max_length=200)
    map = models.OneToOneField(
        Map,
        on_delete=models.CASCADE,
        primary_key=True,
    )
