# Generated by Django 2.2.4 on 2021-05-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_auto_20210523_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='additional',
            field=models.TextField(default='alaa'),
            preserve_default=False,
        ),
    ]