# Generated by Django 4.1 on 2022-08-29 10:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='module',
            fields=[
                ('title', models.CharField(max_length=250)),
                ('Desc', models.TextField(blank=True, null=True)),
                ('module_leader', models.CharField(max_length=250, null=True)),
                ('module_credits', models.IntegerField()),
                ('module_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
