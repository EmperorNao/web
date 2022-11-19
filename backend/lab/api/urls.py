from django.urls import path
from .views import get_services, get_reviews, get_contacts, get_demo_text


urlpatterns = [
    path('services', get_services),
    path('reviews', get_reviews),
    path('contacts', get_contacts),
    path('demo', get_demo_text),
]
