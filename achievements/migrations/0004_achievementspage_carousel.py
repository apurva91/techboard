# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-18 17:09
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0003_achievementsindexpage_carousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievementspage',
            name='carousel',
            field=wagtail.wagtailcore.fields.StreamField((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('quotation', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock())))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())), blank=True),
        ),
    ]
