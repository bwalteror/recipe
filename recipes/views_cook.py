from django.shortcuts import render, redirect
from .models import CookCollector, Category, Recipe

def select_cook(request):
	if request.method == 'POST':
		cook_id = request.POST.get('cook')
		if cook_id:
			return redirect('recipes:cook_home', cook_id=cook_id)
	cooks = CookCollector.objects.all()
	return render(request, 'recipes/select_cook.html', {'cooks': cooks})

def cook_home(request, cook_id):
	cook = CookCollector.objects.get(pk=cook_id)
	categories = Category.objects.filter(cook=cook)
	recipes = Recipe.objects.filter(cook=cook.cook)
	return render(request, 'recipes/cook_home.html', {
		'cook': cook,
		'categories': categories,
		'recipes': recipes
	})
