# Generated by Django 4.0 on 2022-01-05 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0017_document_created_at_document_explaination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialNumberDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='special_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='special_number_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='archive.specialnumberdetail'),
        ),
    ]
