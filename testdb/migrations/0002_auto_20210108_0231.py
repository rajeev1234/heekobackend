# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2021-01-07 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testapplication',
            old_name='aliasId',
            new_name='patner',
        ),
        migrations.RemoveField(
            model_name='testapplication',
            name='externalId',
        ),
        migrations.RemoveField(
            model_name='testapplication',
            name='interestRate',
        ),
        migrations.RemoveField(
            model_name='testapplication',
            name='isTest',
        ),
        migrations.RemoveField(
            model_name='testapplication',
            name='loanamount',
        ),
        migrations.RemoveField(
            model_name='testapplication',
            name='partner',
        ),
        migrations.RemoveField(
            model_name='testapplication',
            name='remainingAmount',
        ),
        migrations.RemoveField(
            model_name='testapplication',
            name='tenure',
        ),
        migrations.RemoveField(
            model_name='testapplication',
            name='trancheId',
        ),
    ]
