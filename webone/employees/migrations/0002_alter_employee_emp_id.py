# Generated by Django 5.2.3 on 2025-07-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(),
        ),
    ]
