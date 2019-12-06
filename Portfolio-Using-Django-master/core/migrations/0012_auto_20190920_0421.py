# Generated by Django 2.2.1 on 2019-09-19 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190920_0344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slideimage',
            old_name='description',
            new_name='description1',
        ),
        migrations.RenameField(
            model_name='slideimage',
            old_name='image',
            new_name='image1',
        ),
        migrations.RemoveField(
            model_name='slideimage',
            name='name',
        ),
        migrations.AddField(
            model_name='slideimage',
            name='description2',
            field=models.CharField(default=1, max_length=100, verbose_name='Images Description 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slideimage',
            name='description3',
            field=models.CharField(default=1, max_length=100, verbose_name='Images Description 3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slideimage',
            name='image2',
            field=models.ImageField(default=1, upload_to='slideimage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slideimage',
            name='image3',
            field=models.ImageField(default=1, upload_to='slideimage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slideimage',
            name='name1',
            field=models.CharField(default=1, max_length=100, verbose_name='Images name 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slideimage',
            name='name2',
            field=models.CharField(default=1, max_length=100, verbose_name='Images name 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slideimage',
            name='name3',
            field=models.CharField(default=1, max_length=100, verbose_name='Images name 3'),
            preserve_default=False,
        ),
    ]
