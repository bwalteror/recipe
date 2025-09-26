from django.core.management.base import BaseCommand
from recipes.models import Recipe

def title_case(s):
    return ' '.join([w.capitalize() for w in s.strip().split()])

class Command(BaseCommand):
    help = 'Trim spaces, title-case name, and set title field with quotes for all recipes.'

    def handle(self, *args, **options):
        updated = 0
        for recipe in Recipe.objects.all():
            # Title-case and trim name
            new_name = title_case(recipe.name)
            # Title field: each word quoted
            quoted_title = f'"{new_name}"'
            # Only update if changed
            if recipe.name != new_name or recipe.title != quoted_title:
                recipe.name = new_name
                recipe.title = quoted_title
                recipe.save()
                updated += 1
        self.stdout.write(self.style.SUCCESS(f'Updated {updated} recipes.'))
