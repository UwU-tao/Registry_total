# Generated by Django 4.2 on 2023-06-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='purpose',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
