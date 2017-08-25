# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-22 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(max_length=250)),
                ('members', wagtail.wagtailcore.fields.StreamField([('evnt', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.CharBlock()), (b'rollno', wagtail.wagtailcore.blocks.IntegerBlock()), (b'phoneno', wagtail.wagtailcore.blocks.IntegerBlock())]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]