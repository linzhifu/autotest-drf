# Generated by Django 2.1 on 2019-09-05 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0067_auto_20190814_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSrcCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=100, verbose_name='案例名称')),
                ('appdes', models.CharField(max_length=50, null=True, verbose_name='案例描述')),
                ('srcname', models.CharField(max_length=100, verbose_name='测试脚本')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最近修改')),
                ('index', models.IntegerField(default=1, verbose_name='测试序号')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Project', verbose_name='所属项目')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name_plural': 'app脚本测试案例',
                'ordering': ('index',),
            },
        ),
    ]
