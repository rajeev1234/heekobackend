# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2021-01-07 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('externalId', models.CharField(blank=True, max_length=50, null=True)),
                ('trancheId', models.CharField(blank=True, max_length=50, null=True)),
                ('aliasId', models.CharField(blank=True, max_length=50, null=True)),
                ('isTest', models.BooleanField(default=False)),
                ('interestRate', models.FloatField(blank=True, null=True)),
                ('tenure', models.IntegerField(blank=True, null=True)),
                ('loanamount', models.FloatField(blank=True, null=True)),
                ('remainingAmount', models.FloatField(blank=True, null=True)),
                ('partner', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestDebitSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateModified', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=1000, null=True)),
                ('modifiedBy', models.CharField(blank=True, max_length=1000, null=True)),
                ('batch_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('emandateId', models.CharField(blank=True, max_length=1000, null=True)),
                ('UMRN', models.CharField(blank=True, max_length=1000, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=1000, null=True)),
                ('errorCode', models.CharField(blank=True, max_length=1000, null=True)),
                ('errorMessage', models.CharField(blank=True, max_length=1000, null=True)),
                ('partner', models.CharField(blank=True, max_length=1000, null=True)),
                ('callbackType', models.CharField(blank=True, max_length=1000, null=True)),
                ('callbackBatchId', models.CharField(blank=True, max_length=1000, null=True)),
                ('callbackUMRN', models.CharField(blank=True, max_length=1000, null=True)),
                ('callbackReceivedDate', models.DateTimeField(blank=True, null=True)),
                ('callbackStatus', models.CharField(blank=True, max_length=1000, null=True)),
                ('callbackErrorCode', models.CharField(blank=True, max_length=1000, null=True)),
                ('callbackErrorDescription', models.CharField(blank=True, max_length=1000, null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testdb.TestApplication')),
            ],
        ),
        migrations.CreateModel(
            name='TestDebitSheetMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateModified', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(blank=True, max_length=1000, null=True)),
                ('result', models.CharField(blank=True, max_length=1000, null=True)),
                ('total_records', models.CharField(blank=True, max_length=1000, null=True)),
                ('records_success', models.CharField(blank=True, max_length=1000, null=True)),
                ('records_failed', models.CharField(blank=True, max_length=1000, null=True)),
                ('partner', models.CharField(blank=True, max_length=1000, null=True)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testdb.TestDebitSheet')),
            ],
        ),
    ]
