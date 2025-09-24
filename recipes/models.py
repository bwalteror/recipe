from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_cards/')
    cook = models.ForeignKey('CookCollector', on_delete=models.CASCADE, related_name='categories', default='Cookie')

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    cook = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    is_favorite = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    title = models.JSONField(blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    meta = models.JSONField(blank=True, null=True)
    ingredients = models.JSONField(blank=True, null=True)
    instructions = models.JSONField(blank=True, null=True)
    notes = models.JSONField(blank=True, null=True)
    comment = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name


class CookCollector(models.Model):
    cook = models.CharField(max_length=50, primary_key=True)  # First name, primary key
    cook_full = models.CharField(max_length=100)  # Full name
    cook_app = models.CharField(max_length=100)  # Name of the collection
    recipe_box_image = models.URLField(max_length=200)  # URL to recipe holder image
    cook_head_shot = models.URLField(max_length=200)  # URL to cook head shot image
    active = models.BooleanField(default=True)  # Whether cook is active and should be shown

    def __str__(self):
        return self.cook_full
