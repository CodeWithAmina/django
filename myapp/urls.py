from .views import simple_form
from django.urls import path


urlpatterns = [
    path('forms/', simple_form,name='form'),
    
]