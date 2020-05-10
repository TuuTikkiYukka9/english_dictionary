from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('sounds/', views.sounds_view, name='sounds'),
    path('irregular_verbs/', views.irregular_verbs_view, name='irregular_verbs'),
    path('dictionary/', views.dictionary_view, name='dictionary'),
    path('translate/', views.translate_view, name='translate'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
