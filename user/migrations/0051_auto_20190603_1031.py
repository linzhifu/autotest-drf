# Generated by Django 2.1.2 on 2019-06-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0050_mpversion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mpversion',
            options={'verbose_name_plural': '测试报告软件版本'},
        ),
        migrations.AddField(
            model_name='mpversion',
            name='MPTool',
            field=models.CharField(default=1, max_length=200, verbose_name='MPTool'),
            preserve_default=False,
        ),
    ]
