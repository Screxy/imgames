# Generated by Django 3.2 on 2022-03-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0010_auto_20220313_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationsettings',
            options={'verbose_name': '[DEV] Настройки организации', 'verbose_name_plural': '[DEV] Настройки организаций'},
        ),
        migrations.AddField(
            model_name='organizationsettings',
            name='money_per_month_default',
            field=models.PositiveIntegerField(default=10000, verbose_name='Количество денег в месяц в комнате по умолчанию'),
        ),
    ]
