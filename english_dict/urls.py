from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sounds/', views.sounds, name='sounds'),
    path('irregular_verbs/', views.irregular_verbs, name='irregular_verbs'),
    path('dictionary/', views.dictionary, name='dictionary'),
]

