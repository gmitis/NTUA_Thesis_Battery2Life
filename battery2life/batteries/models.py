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
    # Unit kWh
    battery_module_energy = models.FloatField(blank=True, null=True, default=0.1)
    # Unit kWh
    battery_usable_energy = models.FloatField(blank=True, null=True, default=0.1)
    # Unit kW
    max_output_power = models.FloatField(blank=True, null=True, default=0.1)
    # Unit kW
    peak_output_power = models.FloatField(blank=True, null=True, default=0.1)
    # Unit V
    nominal_voltage = models.IntegerField(blank=True,null=True,default=0)
    # Unit V
    operating_voltage_range = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000)])
    communication = models.CharField(blank=True, null=True, max_length=40)
    # Unit mm
    power_module_dimension = models.CharField(blank=True, null=True, max_length=40)
    # Unit kg
    power_module_weight = models.FloatField(blank=True, null=True, default=1.0)
    # Unit mm
    battery_module_dimension = models.CharField(blank=True, null=True, max_length=40)
    # Unit kg
    battery_module_weight = models.FloatField(blank=True, null=True, default=1.0)
    # Unit C
    operating_temperature = models.FloatField(validators=[MinValueValidator(-20.0),MaxValueValidator(60.0)])
    # Unit m
    max_operating_altitude = models.IntegerField(blank=True, null=True, default=1)
    # Unit dB
    noise_emission = models.FloatField(blank=True, null=True, default=1.0)
    cell_technology = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    battery = models.ForeignKey(Batteries, on_delete=models.CASCADE, related_name="modules")

    def __str__(self):
        return self.battery_module_name
    

class Cell (models.Model):
    cell_name = models.CharField(max_length=40)
    # Unit Ah
    nominal_capacity = models.IntegerField(blank=True, null=True, default=1)
    # Unit Wh
    nominal_energy = models.IntegerField(blank=True, null=True, default=1)
    cell_chemistry = models.CharField(blank=True, null=True, max_length=40)
    nominal_cycles = models.IntegerField(blank=True, null=True, default=1)
    # Unit Wh/kg
    gravimetric_energy_density = models.IntegerField(blank=True, null=True, default=1)
    # Unit Wh/l
    volumetric_energy_density = models.IntegerField(blank=True, null=True, default=1)
    # (ex LFP71173207)
    industry_standard = models.CharField(blank=True, null=True, max_length=40)
    # Unit V
    nominal_voltage = models.FloatField(blank=True, null=True, default=1.0)
    # Unit V
    operating_voltage = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(10.0)])
    # Unit Megaohm
    ac_resistance = models.FloatField(blank=True, null=True, default=0.1)
    # Unit % / month
    max_self_discharge_rate = models.FloatField(blank=True, null=True, default=1.0)
    # Unit %
    nominal_SOC_at_delivery = models.FloatField(blank=True, null=True, default=1.0)
    # Unit mm (ex 174,7 x 71,65 x 207,11 mm)
    cell_dimension = models.CharField(blank=True, null=True, max_length=40)
    # Unit kg
    cell_weight = models.FloatField(blank=True, null=True, default=1.0)
    # Unit C
    cell_charging_temperature = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(60.0)])
    # Unit C
    cell_discharging_temperature = models.FloatField(validators=[MinValueValidator(-30.0),MaxValueValidator(60.0)])
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="cells")

    def __str__(self):
        return self.cell_name
