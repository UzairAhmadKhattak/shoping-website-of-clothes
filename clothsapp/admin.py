from django.contrib import admin
from .models import home_table,about_us_table,gallery
# Register your models here.
admin.site.register(home_table)
admin.site.register(about_us_table)
admin.site.register(gallery)