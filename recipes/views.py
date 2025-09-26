def recipe_error(request, pk):
    selected_cook = request.session.get('selected_cook')
    recipe = get_object_or_404(Recipe, pk=pk)
    cook_obj = CookCollector.objects.filter(cook=selected_cook).first() if selected_cook else None
    return render(request, 'recipes/recipe_error.html', {'recipe': recipe, 'cook_obj': cook_obj})

# FAQ page view (no pk required)
def faq(request):
    selected_cook = request.session.get('selected_cook')
    cook_obj = CookCollector.objects.filter(cook=selected_cook).first() if selected_cook else None
    return render(request, 'recipes/recipe_error.html', {'cook_obj': cook_obj})
from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe
from selectcook.models import CookCollector
from django.db.models import Q

def category_list(request):
    selected_cook = request.session.get('selected_cook')
    cook_obj = None
    if selected_cook:
        categories = Category.objects.filter(cook__cook=selected_cook).order_by('name')
        cook_obj = CookCollector.objects.filter(cook=selected_cook).first()
    else:
        categories = Category.objects.all().order_by('name')
    return render(request, 'recipes/category_list.html', {'categories': categories, 'cook_obj': cook_obj})

def recipe_list(request, category_name, cook):
    category = get_object_or_404(Category, name=category_name, cook__cook=cook)
    recipes = Recipe.objects.filter(category=category.name, cook=cook).order_by('name')
    cook_obj = CookCollector.objects.filter(cook=cook).first()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'category': category, 'cook_obj': cook_obj})

def recipe_detail(request, pk):
    selected_cook = request.session.get('selected_cook')
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.view_count += 1
    recipe.save()
    cook_obj = CookCollector.objects.filter(cook=selected_cook).first() if selected_cook else None
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'cook_obj': cook_obj})

def search_results(request):
    from django.db.models import Q
    selected_cook = request.session.get('selected_cook')
    query = request.GET.get('q', '')
    search_q = (
        Q(name__icontains=query) |
        Q(title__icontains=query) |
        Q(ingredients__icontains=query) |
        Q(instructions__icontains=query) |
        Q(description__icontains=query) |
        Q(notes__icontains=query) |
        Q(comment__icontains=query)
    )
    if selected_cook:
        recipes = Recipe.objects.filter(search_q, cook=selected_cook).order_by('name')
        cook_obj = CookCollector.objects.filter(cook=selected_cook).first()
    else:
        recipes = Recipe.objects.filter(search_q).order_by('name')
        cook_obj = None
    return render(request, 'recipes/search_results.html', {'recipes': recipes, 'query': query, 'cook_obj': cook_obj})

def favorites_list(request):
    selected_cook = request.session.get('selected_cook')
    if selected_cook:
        recipes = Recipe.objects.filter(is_favorite=True, cook=selected_cook).order_by('name')
        cook_obj = CookCollector.objects.filter(cook=selected_cook).first()
    else:
        recipes = Recipe.objects.filter(is_favorite=True).order_by('name')
        cook_obj = None
    return render(request, 'recipes/favorites_list.html', {'recipes': recipes, 'cook_obj': cook_obj})

def about_page(request):
    return render(request, 'recipes/about.html')