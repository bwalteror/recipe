import csv
from django.core.management.base import BaseCommand
from recipes.models import Recipe, Category

class Command(BaseCommand):
    help = 'Import recipes from index.csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, nargs='?', default='index.csv')

    def handle(self, *args, **kwargs):
        with open(kwargs['csv_file'], newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                category, _ = Category.objects.get_or_create(name=row.get('category', 'Uncategorized'))
                Recipe.objects.create(
                    name=row.get('name', ''),
                    description=row.get('description', ''),
                    category=category,
                    # Add other fields as needed
                )
        self.stdout.write(self.style.SUCCESS('Recipes imported successfully!'))
