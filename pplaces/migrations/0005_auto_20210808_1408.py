# Generated by Django 3.2.6 on 2021-08-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pplaces', '0004_auto_20210806_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ECCCAssignedProjectIdentfer',
            field=models.CharField(max_length=50, unique=True, verbose_name='Proj. Number'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectLocation',
            field=models.ManyToManyField(to='pplaces.ProjectLocation'),
        ),
    ]
