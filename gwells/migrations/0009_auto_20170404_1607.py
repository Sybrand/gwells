# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 23:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0008_auto_20170331_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='diameter',
            field=models.CharField(blank=True, default='', max_length=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='well',
            name='legal_district_lot',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='well',
            name='well_owner_id',
            field=models.ForeignKey(blank=True, db_column='gwells_well_owner_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.WellOwner'),
        ),
    ]
