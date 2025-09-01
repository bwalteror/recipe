import csv
from django.core.management.base import BaseCommand
from recipes.models import Recipe

class Command(BaseCommand):
    help = 'Import recipes from a CSV file and append to the recipes_recipe table.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        count = 0
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Adjust field names below to match your CSV and Recipe model
                Recipe.objects.create(
                    name=row.get('name', ''),
                    category=row.get('category', ''),
                    cook=row.get('cook', ''),
                    image=row.get('image', ''),
                    is_favorite=row.get('is_favorite', 'False').lower() == 'true',
                    view_count=int(row.get('view_count', 0)),
                )
                count += 1
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} recipes from {csv_file}'))
