# Generated by Django 2.1.2 on 2019-06-03 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0052_mpversion_releasenote'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='version',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.MpVersion', verbose_name='软件版本'),
            preserve_default=False,
        ),
    ]
