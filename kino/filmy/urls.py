from django.urls import path
from . import views

app_name = 'filmy'

urlpatterns = [
    path('', views.lista_filmow, name='lista_filmow'),
    path('<int:film_id>/', views.szczegoly_filmu, name='szczegoly_filmu'),
    path('dodaj/', views.dodaj_film, name='dodaj_film'),
    path('filtruj/', views.filtruj_filmy, name='filtruj_filmy'),

]