# Generated by Django 2.1.4 on 2018-12-07 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peach', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='xray_image',
            field=models.ImageField(upload_to='peach'),
        ),
    ]
