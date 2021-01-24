# Generated by Django 3.1.5 on 2021-01-24 07:26

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0008_auto_20210124_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerprofile',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0, 0), srid=4326),
        ),
    ]