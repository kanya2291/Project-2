# Generated by Django 4.2.4 on 2023-09-01 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='des',
            field=models.TextField(max_length=500),
        ),
    ]