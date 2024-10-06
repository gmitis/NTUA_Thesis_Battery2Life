
# todo: add SafetyFeatures extinguising_agent choices  
# todo(optional): add envirnmental, manufacturing fields/models
# todo(optional): add Battery.recycling_info Recycling(critical_raw_materials, safety_measures, dismantling_info(processes), info_prevention_management)

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.SmallIntegerField()
    zipcode = models.SmallIntegerField()
    
    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.city} {self.street} {self.number}"

class Dimensions(models.Model):
    # all metrics in mm
    height = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    width = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    length = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self):
        return f"height:{self.height} width:{self.width} length:{self.length}"
    
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
    chemical_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.chemical_name

    
class SafetyFeatures(models.Model):
    SAFETY_FEATURES = [
        ('tm', 'thermal management'),
        ('op', 'overcharge protection'),
        ('sc', 'short-circuit prevention'),
    ]
    
    safety_feature = models.CharField(max_length=2, choices=SAFETY_FEATURES, null=True)
    
    def __str__(self):
        return self.safety_feature

class Materials(models.Model):
    critical_material = models.BooleanField(default=False)
    recycled_material = models.BooleanField(default=False)
    material = models.CharField(max_length=255)
    
    def __str__(self):
        return self.material



class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.ForeignKey(Address,  null= True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Battery(models.Model):
    serial_number = models.CharField(max_length=255)
    battery_name = models.CharField(max_length=255, blank=True, null=True)
    weight = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0.1) # kilograms
    capacity = models.IntegerField(blank=True, null=True, default=0)  # amp-hours
    original_power_capability = models.IntegerField(blank=True, null=True, default=0)  # Watts
    expected_EndOfLife= models.DateField(blank=True, null=True)
    manufactured_date = models.DateField()
    manufactured_place = models.ForeignKey(
        Address, 
        on_delete=models.PROTECT, 
        blank=True, 
        null=True
    )
    materials = models.ForeignKey(
        Materials, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='batteries'
    )
    safety_features = models.ForeignKey(
        SafetyFeatures, 
        on_delete=models.PROTECT,
        blank=True, 
        null=True, 
        related_name='batteries'
    )
    manufacturer = models.OneToOneField(
        Manufacturer, 
        on_delete=models.CASCADE, 
        related_name="batteries", 
    )
    battery_dimensions = models.OneToOneField(
        Dimensions, 
        on_delete=models.PROTECT, 
        null=True, 
    )

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
    battery_module_dimension = models.OneToOneField(
        Dimensions,
        null=True, 
        on_delete=models.PROTECT, 
        related_name='battery_module_dimension'
    )
    power_module_dimension = models.OneToOneField(
        Dimensions,
        null=True, 
        on_delete=models.PROTECT, 
        related_name='power_module_dimension'
    )
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE, related_name="modules")

    class Meta:
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.battery_module_name


class Cell(models.Model):
    cell_name = models.CharField(max_length=255)
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
    nominal_voltage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=1.0)
    # Unit V
    operating_voltage = models.DecimalField(
        max_digits=20, 
        decimal_places=2, 
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    # Unit Megaohm
    ac_resistance = models.DecimalField(
        max_digits=20, 
        decimal_places=2, 
        blank=True, 
        null=True, 
        default=0.1
    )
    # Unit % / month
    max_self_discharge_rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=1.0)
    # Unit %
    nominal_SOC_at_delivery = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=1.0)
    # Unit kg
    cell_weight = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=1.0)
    # Unit C
    cell_charging_temperature = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0.0), MaxValueValidator(60.0)],
    )
    # Unit C
    cell_discharging_temperature = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(-30.0), MaxValueValidator(60.0)],
    )
    cell_dimension = models.OneToOneField(Dimensions, null=True, on_delete=models.PROTECT)
    cell_chemistry = models.ManyToManyField(Chemical, blank=True, related_name='cells')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="cells")

    class Meta:
        verbose_name_plural = "Cells"

    def __str__(self):
        return self.cell_name


