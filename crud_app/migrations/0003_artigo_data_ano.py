# Generated by Django 5.1.1 on 2024-09-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_remove_artigo_data_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='data_ano',
            field=models.IntegerField(default=2024),
        ),
    ]
