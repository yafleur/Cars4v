from django.contrib import admin

from aplicativo.models import Car

class CarFliter(admin.ModelAdmin):
    list_display = ("id", "user", "model", "brand", "year")
    list_display_links = ("id", "model", "brand", "year")
    list_filter = ("model", "year")
    search_fields = ("model", "brand")
    
# Register your models here.
admin.site.register(Car, CarFliter)
