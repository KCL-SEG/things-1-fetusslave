from django.db import models
from django.core.validators import MaxValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, unique=False, blank=False)
    quantity = models.PositiveSmallIntegerField(validators=[
        MaxValueValidator(100)
    ])
