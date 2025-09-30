from django.db import models

class Temperature(models.Model):
    UNIT_CHOICES = [
        ('C', 'Celsius'),
        ('F', 'Fahrenheit'),
        ('K', 'Kelvin'),
    ]
    
    value = models.FloatField()
    from_unit = models.CharField(max_length=1, choices=UNIT_CHOICES)
    to_unit = models.CharField(max_length=1, choices=UNIT_CHOICES)
    result = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.value} {self.get_from_unit_display()} to {self.get_to_unit_display()}"
