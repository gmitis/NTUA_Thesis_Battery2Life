import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Chemical(models.Model):
    EXTINGUISING_AGENTS =[
        ('fe', 'fire extinguiser'),
    ]
    
    hazardus = models.BooleanField(default=False)
    extinguising_agent = models.CharField(
        max_length=3, 
        choices=EXTINGUISING_AGENTS, 
        blank=True, 
        null=True
    )
    chemical_name = models.CharField(max_length=255, unique=True, default=0)
    
    def __str__(self):
        return self.chemical_name
    
    
class SafetyFeature(models.Model):
    SAFETY_FEATURES = [
        ('tm', 'thermal management'),
        ('op', 'overcharge protection'),
        ('sc', 'short-circuit prevention'),
    ]
    
    safety_feature = models.CharField(max_length=2, choices=SAFETY_FEATURES, default=0)
    
    def __str__(self):
        return self.safety_feature


class Material(models.Model):
    critical_material = models.BooleanField(default=False, blank=True, null=True)
    recycled_material = models.BooleanField(default=False, blank=True, null=True)
    material = models.CharField(max_length=255, default=0)
    
    def __str__(self):
        return self.material

    
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    
    # manufacturer address
    city = models.CharField(max_length=255, default=0)
    street = models.CharField(max_length=255, default=0)
    number = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)
 
    def __str__(self):
        return self.name


class Battery(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    battery_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    weight = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True, default=0.1) # kilograms
    capacity = models.BigIntegerField(blank=True, null=True, default=0)  # amp-hours
    original_power_capability = models.BigIntegerField(blank=True, null=True, default=0)  # Watts
    expected_endoflife = models.DateField(blank=True, null=True)
    manufactured_date = models.DateField(blank=True, null=True)
    
    # batteries dimension
    # all metrics in mm
    height = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)
    width = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)
    length = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)

    # manufacturing facility of the  battery address
    manufactured_city = models.CharField(max_length=255,  blank=True, null=True)
    manufactured_street = models.CharField(max_length=255,  blank=True, null=True)
    manufactured_number = models.IntegerField(blank=True, null=True)
    manufactured_zipcode = models.CharField(max_length=255,  blank=True, null=True)
    
    material = models.ForeignKey(
        Material, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='batteries'
    )
    safety_features = models.ForeignKey(
        SafetyFeature, 
        on_delete=models.PROTECT,
        blank=True, 
        null=True, 
        related_name='batteries'
    )
    manufacturer = models.OneToOneField(
        Manufacturer, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name="batteries", 
    )

    class Meta:
        verbose_name_plural = "Batteries"
    
    def __str__(self):
        return self.serial_number


class Module(models.Model):
    power_module_name = models.CharField(max_length=255)
    battery_module_name = models.CharField(max_length=255)
    # Unit kWh
    battery_module_energy = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True, default=0.1)
    # Unit kWh
    battery_usable_energy = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True, default=0.1)
    # Unit kW
    max_output_power = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True, default=0.1)
    # Unit kW
    peak_output_power = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True, default=0.1)
    # Unit V
    nominal_voltage = models.IntegerField(blank=True, null=True, default=0)
    # Unit V
    operating_voltage_range = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
    communication = models.CharField(blank=True, null=True, max_length=255)
    # Unit kg
    power_module_weight = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=1.0)
    # Unit kg
    battery_module_weight = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=1.0 )
    # Unit C
    operating_temperature = models.FloatField(blank=True,null=True)
    # Unit m
    max_operating_altitude = models.IntegerField(blank=True, null=True, default=1)
    # Unit dB
    noise_emission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=1.0)
    cell_technology = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # module dimension
    # all metrics in mm
    height = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)
    width = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)
    length = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)

    # power_module dimension
    # all metrics in mm
    power_module_height = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)
    power_module_width = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)
    power_module_length = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)

    battery = models.ForeignKey(Battery, blank=True, null=True, on_delete=models.CASCADE, related_name="modules")

    class Meta:
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.battery_module_name


class Cell(models.Model):
    cell_name = models.CharField(max_length=255, unique=True)
    # Unit Ah
    nominal_capacity = models.IntegerField(blank=True, null=True, default=1)
    # Unit Wh
    nominal_energy = models.IntegerField(blank=True, null=True, default=1)
    nominal_cycles = models.IntegerField(blank=True, null=True, default=1)
    # Unit Wh/kg
    gravimetric_energy_density = models.IntegerField(blank=True, null=True, default=1)
    # Unit Wh/l
    volumetric_energy_density = models.IntegerField(blank=True, null=True, default=1)
    # (ex LFP71173207)
    industry_standard = models.CharField(blank=True, null=True, max_length=255)
    # Unit V
    nominal_voltage = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=1.0)
    # Unit V
    operating_voltage = models.DecimalField(
        max_digits=22, 
        decimal_places=2, 
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    # Unit Megaohm
    ac_resistance = models.DecimalField(
        max_digits=22, 
        decimal_places=2, 
        blank=True, 
        null=True, 
        default=0.1
    )
    # Unit % / month
    max_self_discharge_rate = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True, default=1.0)
    # Unit %
    nominal_soc_at_delivery = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True, default=1.0)
    # Unit kg
    cell_weight = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True, default=1.0)
    # Unit C
    cell_charging_temperature = models.DecimalField(
        max_digits=22,
        decimal_places=2,
        blank=True, 
        null=True, 
        validators=[MinValueValidator(0.0), MaxValueValidator(60.0)],
    )
    # Unit C
    cell_discharging_temperature = models.DecimalField(
        max_digits=22,
        decimal_places=2,
        blank=True, 
        null=True, 
        validators=[MinValueValidator(-30.0), MaxValueValidator(60.0)],
    )

    # cell dimension
    # all metrics in mm
    height = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)
    width = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)
    length = models.DecimalField(max_digits=6, decimal_places=2,  blank=True, null=True)

    cell_chemistry = models.ManyToManyField(Chemical, blank=True, related_name='cells')
    module = models.ForeignKey(Module, blank=True, null=True, on_delete=models.CASCADE, related_name="cells")

    class Meta:
        verbose_name_plural = "Cells"

    def __str__(self):
        return self.cell_name


# Cell measurements - synchronous
class Measurement(models.Model):
    voltage = models.FloatField()
    temperature = models.FloatField()
    current = models.FloatField()
    sot = models.FloatField()
    phase = models.FloatField()
    soc = models.FloatField()
    added_at = models.DateTimeField(auto_now_add=True)
    cell_id = models.ForeignKey(Cell, to_field='id', on_delete=models.CASCADE, related_name='measurements')
    
    def __str__(self) -> str:
        return f"{self.id}"
    

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
    cell_id = models.ForeignKey(Cell, to_field='id', on_delete=models.CASCADE, related_name='eis')
    
    class Meta:
        verbose_name_plural="EIS"

    def __str__(self):
        return f"{self.id}"
    