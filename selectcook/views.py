from django.shortcuts import render, redirect
from .models import CookCollector

def select_cook(request):
    cooks = CookCollector.objects.filter(active=True)
    if request.method == 'POST':
        cook_id = request.POST.get('cook')
        if cook_id:
            # Pass cook_id to recipes app (e.g., via session or redirect)
            request.session['selected_cook'] = cook_id
            return redirect('recipes:category_list')
    return render(request, 'selectcook/home.html', {'cooks': cooks})
