from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, unique=False, blank=True)
    quantity = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])
