# Generated by Django 4.2.9 on 2024-03-18 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nip', '0002_client_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.IntegerField(auto_created=True, unique=True),
        ),
    ]
