# Generated by Django 3.1.1 on 2020-09-28 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_auto_20200928_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='text',
            field=models.TextField(max_length=280),
        ),
    ]