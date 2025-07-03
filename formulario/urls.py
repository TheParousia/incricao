from django.urls import path
from .views import formIncricaoPernoite

urlpatterns = [
    path('pernoite/', formIncricaoPernoite, name='form_pernoite'),
]
