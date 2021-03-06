# Generated by Django 4.0 on 2022-01-05 17:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0016_document_project_alter_project_project_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='document',
            name='explaination',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='first_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 5, 17, 23, 50, 265304, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='image_count',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 5, 17, 23, 58, 649419, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='organization_code',
            field=models.CharField(default='IM-2-3-45', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='page_count',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='special_number',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='box',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='folder',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
