from django.contrib import admin
from .models import Category, City, Tip, Restaurant, Payment, Establishments
# Register your models here.

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Tip)
admin.site.register(Restaurant)
admin.site.register(Payment)
admin.site.register(Establishments)
