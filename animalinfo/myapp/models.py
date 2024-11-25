from django.db import models


class Animal(models.Model):
    species = models.CharField(max_length=255)
    habitat = models.CharField(max_length=255)
    diet = models.CharField(max_length=255)
    avg_lifespan = models.IntegerField()
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.species
