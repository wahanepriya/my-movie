# Generated by Django 2.1.7 on 2019-03-09 07:21

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(blank=True, max_length=32, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
