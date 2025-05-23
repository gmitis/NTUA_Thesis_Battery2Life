# Generated by Django 5.0.7 on 2025-02-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batteries', '0003_alter_battery_battery_dimensions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemical',
            name='chemical_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dimension',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='dimension',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='dimension',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='material',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='safetyfeature',
            name='safety_feature',
            field=models.CharField(blank=True, choices=[('tm', 'thermal management'), ('op', 'overcharge protection'), ('sc', 'short-circuit prevention')], max_length=2, null=True),
        ),
    ]
