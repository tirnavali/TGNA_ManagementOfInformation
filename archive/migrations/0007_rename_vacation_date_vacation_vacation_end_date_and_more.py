# Generated by Django 4.0 on 2021-12-31 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0006_vacation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacation',
            old_name='vacation_date',
            new_name='vacation_end_date',
        ),
        migrations.AddField(
            model_name='vacation',
            name='vacation_start_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
