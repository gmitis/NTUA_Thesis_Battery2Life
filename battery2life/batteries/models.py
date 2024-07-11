from django.db import models

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