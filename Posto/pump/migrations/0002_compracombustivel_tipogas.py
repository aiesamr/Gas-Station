# Generated by Django 4.1.1 on 2022-11-20 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pump', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compracombustivel',
            name='tipoGas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pump.bomba'),
        ),
    ]