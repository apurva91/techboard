# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-09 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170908_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpage',
            name='members',
        ),
        migrations.AddField(
            model_name='userpage',
            name='clubname',
            field=models.CharField(choices=[('automobile', 'Automobile'), ('robotics', 'robotics'), ('aeromodelling', 'aeromodelling'), ('electronics', 'electronics'), ('prakriti', 'prakriti'), ('edc', 'EntrepreneurshipDevelopmentCell'), ('fnc', 'FinanceandEconomics'), ('coding', 'CodingClub'), ('astronomy', 'Astronomy'), ('acumen', 'Acumen'), ('radiog', 'RadioG')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='clubname',
            field=models.CharField(choices=[('automobile', 'Automobile'), ('robotics', 'robotics'), ('aeromodelling', 'aeromodelling'), ('electronics', 'electronics'), ('prakriti', 'prakriti'), ('edc', 'EntrepreneurshipDevelopmentCell'), ('fnc', 'FinanceandEconomics'), ('coding', 'CodingClub'), ('astronomy', 'Astronomy'), ('acumen', 'Acumen'), ('radiog', 'RadioG')], max_length=20),
        ),
    ]
