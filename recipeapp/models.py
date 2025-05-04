from django.db import models

class Recipes(models.Model):
    pic = models.FileField(upload_to='recipe_images/')
    title = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.CharField(max_length=200)
    instructions = models.TextField()

# Create your models here.
