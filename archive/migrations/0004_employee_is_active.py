# Generated by Django 4.0 on 2021-12-31 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
