# Generated by Django 4.2.4 on 2023-08-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('des', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('veg', 'Veg'), ('nonveg', 'NonVeg')], default='Veg', max_length=150)),
                ('datee', models.DateField()),
                ('imgg', models.CharField(max_length=500)),
            ],
        ),
    ]
