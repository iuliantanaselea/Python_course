from django.db import models

# Create your models here.
PET_TYPES = [
    ('cat', 'Cat'),
    ('dog', 'Dog'),
    ('rabbit', 'Rabbit')
]


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=1)
    species = models.CharField(max_length=6, choices=PET_TYPES)

    def __str__(self):
        return f"{self.name} - {self.age} - {self.gender} - {self.species}"

