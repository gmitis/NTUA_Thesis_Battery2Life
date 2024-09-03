from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Manufacturer(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Batteries(models.Model):
    serial_number = models.CharField(max_length=40)
    weight = models.FloatField(blank=True,null=True, default=0.1)
    capacity = models.IntegerField(blank=True, null=True, default=0)  #amp-hours
    original_power_capability = models.IntegerField(blank=True, null=True, default=0) #Watts
    manufacture_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='batteries')

    class Meta:
        verbose_name_plural = "Batteries"

    def __str__(self):
        return self.serial_number
    
class Module(models.Model):
    power_module_name = models.CharField(max_length=40)
    battery_module_name = models.CharField(max_length=40)
    battery_module_energy = models.FloatField(blank=True, null=True, default=0.1)
    battery_usable_energy = models.FloatField(blank=True, null=True, default=0.1)
    max_output_power = models.FloatField(blank=True, null=True, default=0.1)
    peak_output_power = models.FloatField(blank=True, null=True, default=0.1)
    nominal_voltage = models.IntegerField(blank=True,null=True,default=0)
    operating_voltage_range = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000)])
    communication = models.CharField(blank=True, null=True, max_length=40)
    power_module_dimension = models.CharField(blank=True, null=True, max_length=40)
    power_module_weight = models.FloatField(blank=True, null=True, default=1.0)
    battery_module_dimension = models.CharField(blank=True, null=True, max_length=40)
    battery_module_weight = models.FloatField(blank=True, null=True, default=1.0)
    operating_temperature = models.FloatField(validators=[MinValueValidator(-20.0),MaxValueValidator(60.0)])
    max_operating_altitude = models.IntegerField(blank=True, null=True, default=1)
    noise_emission = models.FloatField(blank=True, null=True, default=1.0)
    cell_technology = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    battery = models.ForeignKey(Batteries, on_delete=models.CASCADE, related_name="modules")

    def __str__(self):
        return self.battery_module_name