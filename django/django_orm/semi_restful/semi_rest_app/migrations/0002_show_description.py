# Generated by Django 2.2.4 on 2021-05-25 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_rest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default='alaaaaaa'),
            preserve_default=False,
        ),
    ]
