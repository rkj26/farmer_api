# Generated by Django 3.1.5 on 2021-01-23 18:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0002_auto_20210123_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=1000)),
                ('latitude', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
            ],
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='address',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='farmers.userprofile')),
            ],
        ),
    ]