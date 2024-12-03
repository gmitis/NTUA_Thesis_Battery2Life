import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

    
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name


class Battery(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    battery_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    weight = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0.1) # kilograms
    capacity = models.IntegerField(blank=True, null=True, default=0)  # amp-hours
    original_power_capability = models.IntegerField(blank=True, null=True, default=0)  # Watts
    expected_EndOfLife= models.DateField(blank=True, null=True)
    manufactured_date = models.DateField(blank=True, null=True)
    manufactured_place = models.CharField(max_length=2000, null=True, blank=True)
    manufacturer = models.OneToOneField(
        Manufacturer,
        blank=True,
        null=True, 
        on_delete=models.CASCADE, 
        related_name="batteries", 
    )
    battery_dimensions = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Batteries"
        

    def __str__(self):
        return self.serial_number


class Module(models.Model):
    power_module_name = models.CharField(max_length=255)
    battery_module_name = models.CharField(max_length=255)
    # Unit kWh
    battery_module_energy = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=0.1)
    # Unit kWh
    battery_usable_energy = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=0.1)
    # Unit kW
    max_output_power = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=0.1)
    # Unit kW
    peak_output_power = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=0.1)
    # Unit V
    nominal_voltage = models.IntegerField(blank=True, null=True, default=0)
    # Unit V
    operating_voltage_range = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],)
    communication = models.CharField(blank=True, null=True, max_length=255)
    # Unit kg
    power_module_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=1.0)
    # Unit kg
    battery_module_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=1.0 )
    # Unit C
    operating_temperature = models.DecimalField(
        max_digits=3,
        decimal_places=3,
        validators=[MinValueValidator(-20.0), MaxValueValidator(60.0)],
    )
    # Unit m
    max_operating_altitude = models.IntegerField(blank=True, null=True, default=1)
    # Unit dB
    noise_emission = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, default=1.0)
    cell_technology = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    battery_module_dimension = models.CharField(max_length=1000, blank=True, null=True)
    power_module_dimension = models.CharField(max_length=1000, blank=True, null=True)
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE, related_name="modules")

    class Meta:
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.battery_module_name


# class Cell(models.Model):
#     cell_name = models.CharField(max_length=255)
#     # Unit Ah
#     nominal_capacity = models.IntegerField(blank=True, null=True, default=1)
#     # Unit Wh
#     nominal_energy = models.IntegerField(blank=True, null=True, default=1)
#     nominal_cycles = models.IntegerField(blank=True, null=True, default=1)
#     # Unit Wh/kg
#     gravimetric_energy_density = models.IntegerField(blank=True, null=True, default=1)
#     # Unit Wh/l
#     volumetric_energy_density = models.IntegerField(blank=True, null=True, default=1)
#     # (ex LFP71173207)
#     industry_standard = models.CharField(blank=True, null=True, max_length=255)
#     # Unit V
#     nominal_voltage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=1.0)
#     # Unit V
#     operating_voltage = models.DecimalField(
#         max_digits=20, 
#         decimal_places=2, 
#         validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
#     )
#     # Unit Megaohm
#     ac_resistance = models.DecimalField(
#         max_digits=20, 
#         decimal_places=2, 
#         blank=True, 
#         null=True, 
#         default=0.1
#     )
#     # Unit % / month
#     max_self_discharge_rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=1.0)
#     # Unit %
#     nominal_SOC_at_delivery = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=1.0)
#     # Unit kg
#     cell_weight = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=1.0)
#     # Unit C
#     cell_charging_temperature = models.DecimalField(
#         max_digits=20,
#         decimal_places=2,
#         validators=[MinValueValidator(0.0), MaxValueValidator(60.0)],
#     )
#     # Unit C
#     cell_discharging_temperature = models.DecimalField(
#         max_digits=20,
#         decimal_places=2,
#         validators=[MinValueValidator(-30.0), MaxValueValidator(60.0)],
#     )
#     cell_dimension = models.OneToOneField(Dimensions, null=True, on_delete=models.PROTECT)
#     cell_chemistry = models.ManyToManyField(Chemical, blank=True, related_name='cells')
#     module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="cells")

#     class Meta:
#         verbose_name_plural = "Cells"

#     def __str__(self):
#         return self.cell_name


# Pillar1 stakeholder slave cell structure

class Cell(models.Model):
    cell_id = models.PositiveBigIntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'Slave Cell: {self.cell_id}'


# Cell measurements - synchronous
class Measurement(models.Model):
    voltage = models.FloatField()
    temperature = models.FloatField()
    current = models.FloatField()
    sot = models.FloatField()
    phase = models.FloatField()
    soc = models.FloatField()
    added_at = models.DateTimeField(auto_now_add=True)
    cell_id = models.ForeignKey(Cell, to_field='cell_id', on_delete=models.CASCADE, related_name='measurements')
    
    def __str__(self) -> str:
        return self.cell_id
    

# Equivalent Impedance Spectroscopy measurements - asynchronous
class EIS(models.Model):
    status = models.CharField(max_length=255)
    event_id = models.CharField(max_length=255)
    frequency = models.FloatField(validators=[MinValueValidator(0)])
    amplitude = models.FloatField(validators=[MinValueValidator(0)])
    phase = models.FloatField()
    current_offset = models.FloatField()
    v_start = models.FloatField()
    v_end = models.FloatField()
    temperature = models.FloatField(validators=[MinValueValidator(-273.15), MaxValueValidator(5600.0)])
    added_at =models.DateTimeField(auto_now_add=True)
    cell_id = models.ForeignKey(Cell, to_field='cell_id', on_delete=models.CASCADE, related_name='eis')

    def __str__(self):
        return self.cell_id
    