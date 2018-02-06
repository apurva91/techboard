# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-06 11:09
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0002_auto_20180117_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievementsindexpage',
            name='carousel',
            field=wagtail.wagtailcore.fields.StreamField([(b'images', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.CharBlock(blank=True, null=True, required=False))], icon=b'image'))], blank=True),
        ),
    ]