from django.contrib import admin


from users.models import Product, Person

admin.site.register(Product)
admin.site.register(Person)
