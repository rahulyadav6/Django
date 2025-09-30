from django.contrib import admin

# Register your models here.
from .models import Temperature

class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('value', 'from_unit', 'to_unit', 'result', 'created_at')
    search_fields = ('value', 'from_unit', 'to_unit')

admin.site.register(Temperature, TemperatureAdmin)

# create a view named convert_temp that accepts two URL parameters: unit (either "c_to_f" or "f_to_c") and value(temperatue). Based on the unit, the view should convert the temperature from celsiius to fahrenheit or vice versa.
# Example URLs:
# /convert_temp/c_to_f/100 -> 212.0F
# /convert_temp/f_to_c/212 -> 100.0C
# If value is not numeric, return an error message: "invalid temperature value."