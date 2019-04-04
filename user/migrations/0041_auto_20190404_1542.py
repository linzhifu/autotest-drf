# Generated by Django 2.1.2 on 2019-04-04 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0040_auto_20190403_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apicase',
            options={'ordering': ['index'], 'verbose_name_plural': '后端测试案例'},
        ),
        migrations.AlterModelOptions(
            name='apimanager',
            options={'ordering': ['apiname'], 'verbose_name_plural': '后端测试管理'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['proname'], 'verbose_name_plural': '项目信息'},
        ),
        migrations.AddField(
            model_name='apimanager',
            name='result',
            field=models.BooleanField(default=False, verbose_name='测试结果'),
        ),
        migrations.AddField(
            model_name='apimanager',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='最后修改'),
            preserve_default=False,
        ),
    ]