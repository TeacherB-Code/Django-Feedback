from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Review(models.Model):
    username = models.CharField(max_length = 100)
    review_text = models.TextField()
    rating = models.IntegerField()