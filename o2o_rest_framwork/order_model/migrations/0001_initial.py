# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-14 17:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department_model', '0005_recruitmentinformation_is_over'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[(b'w', b'waiting'), (b'a', b'approving'), (b'd', b'denied'), (b's', b'start'), (b'f', b'finishing'), (b'c', b'complaining')], default=b'w', max_length=3)),
                ('is_engineer_review', models.BooleanField(default=False)),
                ('is_department_review', models.BooleanField(default=False)),
                ('applier_message', models.TextField()),
                ('complain_reason', models.TextField(default=None)),
                ('applier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recruitment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department_model.RecruitmentInformation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
