# Generated by Django 4.1.1 on 2022-11-20 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pump', '0002_compracombustivel_tipogas'),
    ]

    operations = [
        migrations.AddField(
            model_name='abastecimento',
            name='placa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pump.veiculo'),
        ),
        migrations.AddField(
            model_name='abastecimento',
            name='tipoGas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pump.bomba'),
        ),
    ]
