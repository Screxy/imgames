# Generated by Django 3.2.12 on 2022-12-26 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0022_alter_queue_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomparticipant',
            name='is_turn_made',
            field=models.BooleanField(default=False, verbose_name='Ход сделан'),
        ),
        migrations.DeleteModel(
            name='Queue',
        ),
    ]
