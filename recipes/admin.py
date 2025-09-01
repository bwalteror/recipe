from django.contrib import admin
from .models import Recipe, Category

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_favorite', 'view_count')
    list_editable = ('is_favorite',)
    readonly_fields = ('view_count',)

admin.site.register(Category)