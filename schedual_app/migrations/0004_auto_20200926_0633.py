# Generated by Django 3.1.1 on 2020-09-26 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedual_app', '0003_auto_20200925_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='disciplines', to='schedual_app.Group'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='teachers',
            field=models.ManyToManyField(blank=True, null=True, related_name='disciplines', to='schedual_app.Teacher'),
        ),
    ]
