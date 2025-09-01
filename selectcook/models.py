from django.db import models

# Create your models here.

class CookCollector(models.Model):
    cook = models.CharField(max_length=32, unique=True, primary_key=True)  # Short name
    cook_full = models.CharField(max_length=128)  # Full name
    cook_app = models.CharField(max_length=64)  # Web app name
    cook_head_shot = models.CharField(max_length=256)  # Headshot image URL
    recipe_box_image = models.CharField(max_length=256)  # Recipe collector image URL
    active = models.BooleanField(default=True)  # Skip if not active

    def __str__(self):
        return self.cook_full
