from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.SmallIntegerField()
    zipcode = models.SmallIntegerField()
    
    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self) -> str:
        return f"{self.city} {self.street} {self.number}"


class Dimensions(models.Model):
    # all metrics in mm
    height = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    width = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    length = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self) -> str:
        return f"height:{self.height} width:{self.width} length:{self.length}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Battery(models.Model):
    serial_number = models.CharField(max_length=255)
    battery_name = models.CharField(max_length=255, blank=True, null=True)
    weight = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0.1) # kilograms
    capacity = models.IntegerField(blank=True, null=True, default=0)  # amp-hours
    original_power_capability = models.IntegerField(blank=True, null=True, default=0)  # Watts
    manufacture_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="batteries", unique=True)
    battery_dimensions = models.OneToOneField(Dimensions, on_delete=models.PROTECT)

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
    nominal_voltage = models.IntegerField(max_digits=4, decimal_places=2, blank=True, null=True, default=0)
    # Unit V
    operating_voltage_range = models.IntegerField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(1000)],)
    communication = models.CharField(blank=True, null=True, max_length=255
    )
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
    battery_module_dimension = models.OneToOneField(Dimensions, on_delete=models.PROTECT)
    power_module_dimension = models.OneToOneField(Dimensions, on_delete=models.PROTECT)
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
    cell_chemistry = models.CharField(blank=True, null=True, max_length=255)
    nominal_cycles = models.IntegerField(blank=True, null=True, default=1)
    # Unit Wh/kg
    gravimetric_energy_density = models.IntegerField(blank=True, null=True, default=1)
    # Unit Wh/l
    volumetric_energy_density = models.IntegerField(blank=True, null=True, default=1)
    # (ex LFP71173207)
    industry_standard = models.CharField(blank=True, null=True, max_length=255)
    # Unit V
    nominal_voltage = models.DecimalField(blank=True, null=True, default=1.0)
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
    cell_dimension = models.OneToOneField(Dimensions, on_delete=models.PROTECT)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="cells")

    class Meta:
        verbose_name_plural = "Cells"

    def __str__(self):
        return self.cell_name


