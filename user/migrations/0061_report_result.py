# Generated by Django 2.1.2 on 2019-06-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0060_auto_20190605_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='result',
            field=models.CharField(default=1, max_length=800, verbose_name='测试结果汇总'),
            preserve_default=False,
        ),
    ]
