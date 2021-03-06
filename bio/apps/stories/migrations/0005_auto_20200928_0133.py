# Generated by Django 3.1.1 on 2020-09-28 01:33

from django.db import migrations, models
import django.utils.timezone
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20200928_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='position',
        ),
        migrations.AddField(
            model_name='stage',
            name='position',
            field=positions.fields.PositionField(default=-1),
        ),
        migrations.AddField(
            model_name='story',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
