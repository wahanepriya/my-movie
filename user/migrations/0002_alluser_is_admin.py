# Generated by Django 2.1.7 on 2019-03-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alluser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]