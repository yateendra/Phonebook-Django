from django.urls import path
from .views import phonebook,add_contact, edit_contact, delete_contact

urlpatterns = [
    path('', phonebook, name='phonebook'),
    path('add/', add_contact, name='add_contact'),
    path('edit/<int:pk>/', edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>/', delete_contact, name='delete_contact')
    
]
