from django.db import models
from datetime import timedelta

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.PositiveIntegerField(default=1)
    prep_time = models.DurationField(default=timedelta(minutes=30))
    cook_time = models.DurationField(default=timedelta(minutes=30))

    def __str__(self):
        return self.title
