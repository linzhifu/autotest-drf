# Generated by Django 2.1.2 on 2019-04-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_auto_20190403_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='apicase',
            name='apiname1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='接口名称'),
        ),
    ]
