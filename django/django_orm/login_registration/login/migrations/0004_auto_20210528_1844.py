# Generated by Django 2.2.4 on 2021-05-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210528_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
