# Generated by Django 5.0 on 2024-03-31 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_dataproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataproject',
            name='demo',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
