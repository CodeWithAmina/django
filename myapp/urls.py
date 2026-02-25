from django.urls import path
from .views import contact_create, contact_list, contact_detail, contact_update, contact_delete


urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/create/', contact_create, name='contact_create'),
    path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('contacts/<int:pk>/update/', contact_update, name='contact_update'),
    path('contacts/<int:pk>/delete/', contact_delete, name='contact_delete'),
]