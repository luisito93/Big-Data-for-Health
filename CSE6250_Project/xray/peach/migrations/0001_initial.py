# Generated by Django 2.1.4 on 2018-12-07 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=200)),
                ('xray_image', models.ImageField(upload_to='static/documents/')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('pre_result', models.CharField(max_length=200)),
            ],
        ),
    ]
