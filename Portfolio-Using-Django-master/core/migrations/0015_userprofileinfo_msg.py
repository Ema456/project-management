# Generated by Django 3.0a1 on 2019-09-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='msg',
            field=models.CharField(default=1, max_length=100, verbose_name='msg'),
            preserve_default=False,
        ),
    ]
