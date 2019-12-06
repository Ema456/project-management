# Generated by Django 2.2.6 on 2019-11-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20191025_0406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
            ],
        ),
    ]