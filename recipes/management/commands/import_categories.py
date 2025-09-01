import csv
from django.core.management.base import BaseCommand
from recipes.models import Category
from selectcook.models import CookCollector

class Command(BaseCommand):
    help = 'Import categories from a CSV file and append to the Category table.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        count = 0
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Adjust field names below to match your CSV and Category model
                cook_key = row.get('cook_id', '')
                cook_obj = CookCollector.objects.filter(cook=cook_key).first() if cook_key else None
                Category.objects.create(
                    name=row.get('name', ''),
                    image=row.get('image', ''),
                    cook=cook_obj
                )
                count += 1
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} categories from {csv_file}'))
