# Generated by Django 2.1.2 on 2019-04-06 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0043_auto_20190406_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-update_time'], 'verbose_name_plural': '项目信息'},
        ),
    ]