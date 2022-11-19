from django.contrib import admin
from .models import Service, Review, Contact, Link


admin.site.register(Review)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Link)
