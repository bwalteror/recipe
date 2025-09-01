import csv
import os
from django.core.management.base import BaseCommand
from recipes.models import Category, Recipe, CookCollector
from django.conf import settings

class Command(BaseCommand):
    help = 'Import recipes from index.csv'

    def handle(self, *args, **kwargs):
        # Ensure default CookCollector exists
        cook_collector, _ = CookCollector.objects.get_or_create(
            cook='Cookie',
            defaults={
                'cook_full': 'Cookie Default',
                'cook_app': "Cookie's Collection",
                'recipe_box_image': '',
                'cook_head_shot': ''
            }
        )

        with open('index.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                category_name = row['category']
                category_image_path = None
                for ext in ['.jpg', '.png']:
                    path = f'category_cards/{category_name}{ext}'
                    if os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
                        category_image_path = path
                        break

                category, _ = Category.objects.get_or_create(
                    name=category_name,
                    cook=cook_collector
                )
                if category_image_path:
                    category.image.name = category_image_path
                    category.save()

                recipe = Recipe(
                    name=row['recipe_name'],
                    category=category,
                    cook=cook_collector
                )
                recipe.image.name = f'images/{row["image_file_1"]}'
                recipe.save()