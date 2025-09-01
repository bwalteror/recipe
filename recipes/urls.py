
app_name = 'recipes'
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<str:category_name>/<str:cook>/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('search/', views.search_results, name='search_results'),
    path('favorites/', views.favorites_list, name='favorites_list'),
    path('about/', views.about_page, name='about_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
